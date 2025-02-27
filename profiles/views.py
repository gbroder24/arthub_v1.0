from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order

# Create your views here.


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    # Get the order object or return 404 if not found
    order = get_object_or_404(Order, order_number=order_number)

    # Check if the order is linked to a user profile
    if order.user_profile:
        # This is an order placed by a logged-in user
        try:
            # Try to get the user profile for the logged-in user
            profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            messages.error(request, "User profile not found.")
            return render(request, "errors/404.html", status=404)

        # Check if the logged-in user has permission to view the order
        if order.user_profile != profile:
            messages.error(
                request, "You do not have permission to view this order.")
            return render(request, "errors/404.html", status=404)

    else:
        # If the order is anonymous, prevent a logged-in user from viewing it
        if request.user.is_authenticated:
            messages.error(request, "You cannot view an anonymous order.")
            return render(request, "errors/404.html", status=404)

    # Success message for valid order
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    # Return the success page with the order context
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

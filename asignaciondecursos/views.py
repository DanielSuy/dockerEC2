import stripe
from django.shortcuts import render, redirect
from .asignaciondecursos import Asignaciondecursos
from estudiante.models import Curso
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.

def agregar_curso(request, curso_id):

    asignaciondecursos=Asignaciondecursos(request)
    curso=Curso.objects.get(id=curso_id)
    asignaciondecursos.agregar(curso=curso)
    return redirect("Estudiante")

def eliminar_curso(request, curso_id):

    asignaciondecursos=Asignaciondecursos(request)
    curso=Curso.objects.get(id=curso_id)
    asignaciondecursos.eliminar(curso=curso)
    return redirect("Estudiante")


def restar_curso(request, curso_id):
    asignaciondecursos=Asignaciondecursos(request)
    curso=Curso.objects.get(id=curso_id)
    asignaciondecursos.restar_curso(curso=curso)
    return redirect("Estudiante")


def limpiar_asignaciondecursos(request, curso_id):
    asignaciondecursos=Asignaciondecursos(request)
    asignaciondecursos.limpiar_asignaciondecursos()
    return redirect("Estudiante")

"""
def procesar_pago(request):
    if request.method == 'POST':
        # Recuperar la información del formulario de pago
        nombre_tarjeta = request.POST.get('nombre_tarjeta')
        numero_tarjeta = request.POST.get('numero_tarjeta')
        codigo = request.POST.get('codigo')

        try:
            # Crear un token de tarjeta con Stripe
            token = stripe.Token.create(
                card={
                    'number': numero_tarjeta,
                    'cvc': codigo,
                    'name': nombre_tarjeta,
                },
            )

            # Realizar el pago con el token
            charge = stripe.Charge.create(
                amount=1000,  # El monto en centavos (ejemplo: $10.00)
                currency='Q',
                description='Compra de cursos',
                source=token.id,
            )

            # Pago exitoso, redirige a la página de confirmación
            messages.success(request, '¡Pago exitoso!')
            return redirect('pago_exitoso.html')

        except stripe.error.CardError as e:
            # Error en la tarjeta, muestra un mensaje de error
            messages.error(request, f'Error al procesar el pago: {e.error.message}')
        except stripe.error.StripeError as e:
            # Otro error de Stripe, muestra un mensaje de error general
            messages.error(request, 'Error al procesar el pago. Inténtalo nuevamente.')

    # Si no es una solicitud POST o el pago falló, renderiza el formulario de pago
    return render(request, 'formulario_pago.html')

def pago_exitoso(request):
    # Lógica para obtener la dirección de correo electrónico del usuario, por ejemplo, desde el objeto User
    email_usuario = request.user.email

    # Enviar correo electrónico de confirmación
    send_mail(
        'Pago Exitoso',
        'Gracias por tu compra. Tu pago ha sido procesado exitosamente.',
        settings.DEFAULT_FROM_EMAIL,
        [email_usuario],
        fail_silently=False,
    )

    # Renderizar la plantilla de pago exitoso
    return render(request, 'asignaciondecursos/pago_exitoso.html')
    """

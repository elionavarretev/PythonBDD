from behave import given, when, then
from tests.features.pages.esikaPageObjects import EsikaPageObjects
from tests.framework.webapp import webapp


@given(u'que un invitado y entra a la web esika')
def step_impl_web(context):
    webapp.load_website()


@given(u'además, selecciona "{categoria}" y selecciona "{tipo}"')
def step_impl_ademasselecciona(context, categoria, tipo):
    EsikaPageObjects().seleccionarCategoria(categoria)
    EsikaPageObjects().seleccionarTipo(tipo)


@when(u'se dirige a la ficha del producto "{cualquiera}"')
def step_impl_seDirigeALaFichaDelProducto(context, cualquiera):
    EsikaPageObjects().ingresarFichaDelProducto(cualquiera)


@when(u'agrega "{cantidad}" adicional')
def step_impl_agregaAdicional(context, cantidad):
    EsikaPageObjects().agregarCantidad(cantidad)


@then(u'agrega a la bolsa')
def step_impl_agregaALaBolsa(context):
    EsikaPageObjects().seleccionarAgregarBolsa()


@then(u'se registra como "{invitado}')
def step_impl_seRegistraComoInvitado(context, invitado):
    EsikaPageObjects().seleccionarIrPagarPopPup()
    EsikaPageObjects().seleccionarIrPagar()
    EsikaPageObjects().ingresarComoInvitado(invitado)



@then(u'se registra la dirección de "{envio}" y anula la compra')
def step_impl_seRegistraLaDirecciónDeYAnulaLaCompra(context, envio):
    EsikaPageObjects().ingresarDireccionEnvio(envio)


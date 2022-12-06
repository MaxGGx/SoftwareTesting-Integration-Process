*** Variables ***

${HOSTNAME}             localhost
${PORT}                 8000
${SERVER}               http://${HOSTNAME}:${PORT}/
${BROWSER}              chrome


*** Settings ***

Documentation   Django Robot Tests
Library         SeleniumLibrary  timeout=15  implicit_wait=0
Library         DjangoLibrary  ${HOSTNAME}  ${PORT}  path=mysite/mysite  manage=manage.py  settings=recetario.settings
Suite Setup     open Browserr
Suite Teardown  close browserr

*** Keywords ***

open Browserr
  Open Browser  ${SERVER}  ${BROWSER}

close browserr
  Close Browser


*** Test Cases ***

Scenario: Agregar receta
  Go To  ${SERVER}
  Wait until page contains element  id=explanation
  Page Should Contain  Ver recetas
  Click Button  id:anadirReceta
  Page Should Contain  Añadir receta
  Input Text  name:nombreReceta  Sopaipilla
  Input Text  name:ingredientes  Harina\nHuevos\nZapallo
  Input Text  name:pasos  Paso1\nPaso2\nPaso3\n
  Input Text  name:autor  ABCDEFGHIJKLMNOPQRSTUVWXYZABCD1234
  Choose File  name:imagenReceta  ${CURDIR}/sopaipilla.jpg
  Wait Until Element Is Not Visible  id:failed-alert
  Click Button  Subir Receta
  Wait Until Element Is Visible  id:success-alert
  Wait Until Element Is Not Visible  id:success-alert

Scenario: Ver receta
  Go To  ${SERVER}
  Wait until page contains element  id=explanation
  Page Should Contain  Ver recetas
  Page Should Contain  Sopaipilla
  Click Link  name:verReceta
  Page Should Contain  Preparacion:

Scenario: Actualizar receta
  Go To  ${SERVER}
  Wait until page contains element  id=explanation
  Page Should Contain  Ver recetas
  Page Should Contain  Sopaipilla
  Click Link  name:verReceta
  Page Should Contain  Preparacion:
  Click Button  id:editarReceta
  Page Should Contain  Editar receta
  Input Text  name:nombreReceta  Sopaipilla2
  Choose File  name:imagenReceta  ${CURDIR}/sopaipilla.jpg
  Click Button  Editar Receta
  Wait Until Element Is Visible  id:success-alert
  Wait Until Element Is Not Visible  id:success-alert
  Click Button  id:verRecetas
  Page Should Contain  Ver recetas
  Page Should Contain  Sopaipilla2

Scenario: Eliminar receta
  Go To  ${SERVER}
  Wait until page contains element  id=explanation
  Page Should Contain  Ver recetas
  Page Should Contain  Sopaipilla2
  Click Link  name:verReceta
  Page Should Contain  Preparacion:
  Click Button  id:eliminarReceta
  Page Should Contain  Ver recetas
  Page Should Not Contain  Sopaipilla2

Scenario: Agregar una receta con el formato incorrecto - Ingredientes
  Go To  ${SERVER}
  Wait until page contains element  id=explanation
  Page Should Contain  Ver recetas
  Click Button  id:anadirReceta
  Page Should Contain  Añadir receta
  Input Text  name:nombreReceta  Sopaipilla
  Input Text  name:ingredientes  Harina Huevos Zapallo
  Input Text  name:pasos  Paso1\nPaso2\nPaso3
  Input Text  name:autor  ROBOT
  Choose File  name:imagenReceta  ${CURDIR}/sopaipilla.jpg
  Click Button  Subir Receta
  Element Should Be Visible  id:failed-alert
  Wait Until Element Is Not Visible  id:failed-alert

Scenario: Agregar una receta con el formato incorrecto - Pasos
  Go To  ${SERVER}
  Wait until page contains element  id=explanation
  Page Should Contain  Ver recetas
  Click Button  id:anadirReceta
  Page Should Contain  Añadir receta
  Input Text  name:nombreReceta  Sopaipilla
  Input Text  name:ingredientes  Harina\nHuevos\nZapallo
  Input Text  name:pasos  Paso1 Paso2 Paso3
  Input Text  name:autor  ROBOT
  Choose File  name:imagenReceta  ${CURDIR}/sopaipilla.jpg
  Wait Until Element Is Not Visible  id:failed-alert
  Click Button  Subir Receta
  Element Should Be Visible  id:failed-alert
  Wait Until Element Is Not Visible  id:failed-alert

Scenario: Agregar una receta con falta de información - Imagen
  Go To  ${SERVER}
  Wait until page contains element  id=explanation
  Page Should Contain  Ver recetas
  Click Button  id:anadirReceta
  Page Should Contain  Añadir receta
  Input Text  name:nombreReceta  Sopaipilla
  Input Text  name:ingredientes  Harina\nHuevos\nZapallo
  Input Text  name:pasos  Paso1\nPaso2\nPaso3
  Input Text  name:autor  ROBOT
  Wait Until Element Is Not Visible  id:failed-alert
  Click Button  Subir Receta
  Element Should Not Be Visible  id:success-alert

Scenario: Agregar receta correcta + editar + limite de campos + eliminar
  Go To  ${SERVER}
  Wait until page contains element  id=explanation
  Page Should Contain  Ver recetas
  Click Button  id:anadirReceta
  Page Should Contain  Añadir receta
  Input Text  name:nombreReceta  Sopaipilla
  Input Text  name:ingredientes  Harina\nHuevos\nZapallo
  Input Text  name:pasos  Paso1\nPaso2\nPaso3\n
  Input Text  name:autor  ABCDEFGHIJKLMNOPQRSTUVWXYZABCD1234
  Choose File  name:imagenReceta  ${CURDIR}/sopaipilla.jpg
  Wait Until Element Is Not Visible  id:failed-alert
  Click Button  Subir Receta
  Wait Until Element Is Visible  id:success-alert
  Wait Until Element Is Not Visible  id:success-alert
  Click Button  id:verRecetas
  Page Should Contain  Ver recetas
  Page Should Contain  Sopaipilla
  Click Link  name:verReceta
  Page Should Contain  Preparacion:
  Page Should Contain  Por: ABCDEFGHIJKLMNOPQRSTUVWXYZABCD
  Click Button  id:editarReceta
  Page Should Contain  Editar receta
  Input Text  name:nombreReceta  Sopaipilla2
  Choose File  name:imagenReceta  ${CURDIR}/sopaipilla.jpg
  Click Button  Editar Receta
  Wait Until Element Is Visible  id:success-alert
  Wait Until Element Is Not Visible  id:success-alert
  Click Button  id:verRecetas
  Page Should Contain  Ver recetas
  Page Should Contain  Sopaipilla2
  Click Link  name:verReceta
  Page Should Contain  Preparacion:
  Click Button  id:eliminarReceta
  Page Should Contain  Ver recetas
  Page Should Not Contain  Sopaipilla2

Scenario: Agregar 11 recetas seguidas
  Go To  ${SERVER}
  Wait until page contains element  id=explanation
  Page Should Contain  Ver recetas
  Click Button  id:anadirReceta
  Page Should Contain  Añadir receta
  FOR  ${i}  IN RANGE  1    12
    Input Text  name:nombreReceta  Sopaipilla${i}
    Input Text  name:ingredientes  Harina\nHuevos\nZapallo
    Input Text  name:pasos  Paso1\nPaso2\nPaso3\n
    Input Text  name:autor  ABCDEFGHIJKLMNOPQRSTUVWXYZABCD1234
    Choose File  name:imagenReceta  ${CURDIR}/sopaipilla.jpg
    Wait Until Element Is Not Visible  id:failed-alert
    Click Button  Subir Receta
    Wait Until Element Is Visible  id:success-alert
    Wait Until Element Is Not Visible  id:success-alert
  END
  Click Button  id:verRecetas
  Page Should Contain  Ver recetas
  Page Should Contain  Sopaipilla1
  Page Should Contain  Sopaipilla2
  Page Should Contain  Sopaipilla3
  Page Should Contain  Sopaipilla4
  Page Should Contain  Sopaipilla5
  Page Should Contain  Sopaipilla6
  Page Should Contain  Sopaipilla7
  Page Should Contain  Sopaipilla8
  Page Should Contain  Sopaipilla9
  Page Should Contain  Sopaipilla10
  Page Should Contain  Sopaipilla11
  FOR  ${b}  IN RANGE  1    12
    Click Link  name:verReceta
    Page Should Contain  Preparacion:
    Click Button  id:eliminarReceta
    Page Should Contain  Ver recetas
  END

  

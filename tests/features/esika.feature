#AUTOMATION: elionavarretev@gmail.com
Feature: AUTOMATION

  Scenario Outline: Flujo
    Given que un invitado y entra a la web esika
    And además, selecciona "<categoria>" y selecciona "<tipo>"
    When se dirige a la ficha del producto "<cualquiera>"
    And agrega "<cantidad>" adicional
    Then agrega a la bolsa
    And se registra como "<invitado>"
    And se registra la dirección de "<envio>" y anula la compra
    Examples:
      | categoria | tipo |cualquiera| cantidad | invitado | envio |
      | Perfumes| Maderosa |200097966 |2 | Elio;Navarrete;elionavarretev@gmail.com;elionavarretev@gmail.com|PE-DEP-05;05-AIJA;AIJA-AIJA;Av Larco 23;AA;Plaza Vea;979094101|

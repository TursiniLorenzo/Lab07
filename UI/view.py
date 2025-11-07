from msilib.schema import ListView

import flet as ft
from flet.core.dropdown import Dropdown

from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()


    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        self._dd_nomi = Dropdown (label = "Nome Museo",
                                  options = self.controller.popola_con_musei())

        self._dd_epoche = Dropdown (label = "Epoche",
                                    options = self.controller.popola_con_epoche(),
                                    width = 200)
        # Sezione 3: Artefatti
        self._txt_lista = ft.Text (value = "Lista Artefatti",
                                   size = 20,
                                   weight = ft.FontWeight.BOLD)

        self._lst_artefatti = ft.ListView (expand = True,
                                           controls = [ft.Text ("Seleziona un museo ed un'epoca per iniziare.")])

        def aggiorna_lista_artefatti(e):
            self.controller.museo_selezionato = self._dd_nomi.value
            self.controller.epoca_selezionata = self._dd_epoche.value

            lista_artefatti = self.controller.mostra_artefatti(self.controller.museo_selezionato,
                                                               self.controller.epoca_selezionata)

            lista_artefatti_per_museo = self.controller.mostra_artefatti_per_museo(self.controller.museo_selezionato)
            lista_artefatti_per_epoca = self.controller.mostra_artefatti_per_epoca(self.controller.epoca_selezionata)

            tutti_artefatti = self.controller.mostra_tutti_artefatti()

            dati_artefatti = []
            if lista_artefatti:
                for artefatto in lista_artefatti:
                    dati_artefatti.append(ft.ListTile(title=ft.Text(artefatto.nome)))
                    self._txt_lista.value = f"Lista Artefatti {self.controller.museo_selezionato}, {self.controller.epoca_selezionata}"
            else:
                if self.controller.museo_selezionato and self.controller.epoca_selezionata:
                    dati_artefatti.append(ft.Text("Nessun risultato trovato."))
                    self._txt_lista.value = f"Lista Artefatti {self.controller.museo_selezionato}, {self.controller.epoca_selezionata}"

                elif self.controller.museo_selezionato and not self.controller.epoca_selezionata:
                    for artefatto in lista_artefatti_per_museo:
                        dati_artefatti.append(ft.ListTile(title=ft.Text(artefatto)))
                        self._txt_lista.value = f"Lista Artefatti {self.controller.museo_selezionato}"

                elif self.controller.epoca_selezionata and not self.controller.museo_selezionato:
                    for artefatto in lista_artefatti_per_epoca:
                        dati_artefatti.append(ft.ListTile(title=ft.Text(artefatto)))
                        self._txt_lista.value = f"Lista Artefatti {self.controller.epoca_selezionata}"

                elif not self.controller.museo_selezionato and not self.controller.epoca_selezionata:
                    for artefatto in tutti_artefatti:
                        dati_artefatti.append(ft.ListTile(title=ft.Text(artefatto)))
                        self._txt_lista.value = f"Lista Artefatti"

            self._lst_artefatti.controls = dati_artefatti
            self._lst_artefatti.update ()
            self._txt_lista.update ()

            self._dd_nomi.value = None
            self._dd_epoche.value = None

            self.page.update()


        self.btn_mostra_artefatti = ft.ElevatedButton ("Mostra artefatti",
                                                       on_click= aggiorna_lista_artefatti)

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            ft.Row (spacing = 100,
                    controls = [self._dd_nomi, self._dd_epoche],
                    alignment = ft.MainAxisAlignment.CENTER),

            # Sezione 3: Artefatti
            ft.Divider (),
            self.btn_mostra_artefatti,
            self._txt_lista,
            self._lst_artefatti,
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()

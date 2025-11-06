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
        # TODO
        self._dd_nomi = Dropdown (label = "Nome Museo",
                                  options = self.controller.popola_con_musei())

        self._dd_epoche = Dropdown (label = "Epoche",
                                    options = self.controller.popola_con_epoche(),
                                    width = 200)
        # Sezione 3: Artefatti
        # TODO
        self._lst_artefatti = ft.ListView (expand = True,
                                           controls = [ft.Text ("Seleziona un museo ed un'epoca per iniziare.")])

        def aggiorna_lista_artefatti (e) :
            self.controller.museo_selezionato = self._dd_nomi.value.strip()
            self.controller.epoca_selezionata = self._dd_epoche.value.strip()

            lista_artefatti = self.controller.mostra_artefatti(self.controller.museo_selezionato, self.controller.epoca_selezionata)

            dati_artefatti = []
            if lista_artefatti :
                for artefatto in lista_artefatti :
                    dati_artefatti.append(ft.ListTile (title =ft.Text(artefatto.nome)))
            else :
                if self.controller.museo_selezionato and self.controller.epoca_selezionata :
                    dati_artefatti.append (ft.Text ("Nessun risultato trovato."))
                else :
                    dati_artefatti.append (ft.Text ("Seleziona entrambi i filtri."))

            self._lst_artefatti.controls = dati_artefatti
            self._lst_artefatti.update ()
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
            # TODO
            ft.Row (spacing = 100,
                    controls = [self._dd_nomi, self._dd_epoche],
                    alignment = ft.MainAxisAlignment.CENTER),

            # Sezione 3: Artefatti
            # TODO
            ft.Divider (),
            self.btn_mostra_artefatti,
            self._lst_artefatti,
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()

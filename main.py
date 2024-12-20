from usuarios import Usuario
from publicaciones import Publicacion
from comentarios import Comentario


class Menu:
    def __init__(self):
        self.id_usuario = None
        self.usuario = Usuario()
        self.publicacion = Publicacion()
        self.comentario = Comentario()

    def mostrar_menu(self):
        while True:
            if self.id_usuario:
                self.mostrar_menu_usuario_logueado()
            else:
                self.mostrar_menu_usuario_no_logueado()

#Sirve para mostrar el menu para usuario logeado
    def mostrar_menu_usuario_logueado(self):
        """Menú para usuarios logueados."""
        print("""
            1. Registrarse
            2. Iniciar sesión
            3. Ver publicaciones
            4. Crear publicación
            5. Editar publicación
            6. Eliminar publicación
            7. Ver comentarios
            8. Crear comentario
            9. Editar comentario
            10. Eliminar comentario
            11. Buscar video por título
            0. Salir
        """)
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            self.usuario.registrar_usuario()
        elif opcion == "2":
            print("Ya has iniciado sesión.")
        elif opcion == "3":
            self.publicacion.leer_publicaciones()
        elif opcion == "4":
            self.publicacion.crear_publicacion(self.id_usuario)
        elif opcion == "5":
            self.publicacion.actualizar_publicacion(self.id_usuario)
        elif opcion == "6":
            self.publicacion.eliminar_publicacion(self.id_usuario)
        elif opcion == "7":
            self.publicacion.leer_publicaciones()
            id_publicacion = input("\nIntroduce el ID de la publicación para ver los comentarios: ")
            self.comentario.leer_comentarios(id_publicacion)
        elif opcion == "8":
            self.comentario.crear_comentario(self.id_usuario)
        elif opcion == "9":
            self.comentario.actualizar_comentario(self.id_usuario)
        elif opcion == "10":
            self.comentario.eliminar_comentario(self.id_usuario)
        elif opcion == "11":
            self.publicacion.buscar_video_por_titulo()
        elif opcion == "0":
            print("Saliendo del programa...")
            exit()
        else:
            print("Opción no válida. Inténtalo de nuevo.")
#mostrar menu de usuario no logeado
    def mostrar_menu_usuario_no_logueado(self):
        """Menú para usuarios no logueados."""
        print("""
            1. Registrarse
            2. Iniciar sesión
            3. Ver publicaciones
            4. Ver comentarios
            5. Crear comentario
            6. Buscar video por título
            0. Salir
        """)
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            self.usuario.registrar_usuario()
        elif opcion == "2":
            self.id_usuario = self.usuario.iniciar_sesion()
        elif opcion == "3":
            self.publicacion.leer_publicaciones()
        elif opcion == "4":
            id_publicacion = input("\nIntroduce el ID de la publicación para ver los comentarios: ")
            self.comentario.leer_comentarios(id_publicacion)
        elif opcion == "5":
            print("\nDebes registrarte o iniciar sesión para crear un comentario.")
            self.mostrar_menu_autenticacion()
        elif opcion == "6":
            self.publicacion.buscar_video_por_titulo()
        elif opcion == "0":
            print("Saliendo de tiktok..")
            exit()
        else:
            print("Opción no válida. Inténtalo de nuevo.")

    def mostrar_menu_autenticacion(self):
        """Menú para redirigir a registro o inicio de sesión."""
        while True:
            print("""
                1. Registrarse
                2. Iniciar sesión
                0. Volver al menú principal
            """)
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.usuario.registrar_usuario()
                break
            elif opcion == "2":
                self.id_usuario = self.usuario.iniciar_sesion()
                break
            elif opcion == "0":
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu()

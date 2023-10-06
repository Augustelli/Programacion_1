import { Component } from '@angular/core';
import { UsuariosService } from 'src/app/services/usuarios.service';
import { HttpClient } from '@angular/common/http';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-crear-usuario-admin',
  templateUrl: './crear-usuario-admin.component.html',
  styleUrls: ['./crear-usuario-admin.component.css']
})
export class CrearUsuarioAdminComponent {
  formData: any = {};

  constructor(
    private usuariosService: UsuariosService,
    private router: Router
  ){}
  onSubmit(form: NgForm) { // Añade NgForm como argumento
    const fechaNacimiento = this.formatDate(this.formData.fecha_nacimiento);

    const newUserData = {
      ...this.formData,
      fecha_nacimiento: fechaNacimiento};
    // const formData = form.value; // Obtiene los datos del formulario
    this.usuariosService.createUser({ ...newUserData})
      .subscribe(
        (response) => {
          console.log('Solicitud POST exitosa', response);

          // Realiza acciones adicionales si es necesario, como redirigir a otra página o mostrar un mensaje de éxito
        },
        (error) => {
          console.error('Error en la solicitud POST', error);
          // Maneja el error de acuerdo a tus necesidades
        }
      );
  }
  formatDate(date: string): string {
    const parts = date.split('-');
    if (parts.length === 3) {
      const [year, month, day] = parts;
      return `${day}-${month}-${year}`;
    }
    return date;
  }
  goBack() {
    this.router.navigate(['/usuarios']);
}
}


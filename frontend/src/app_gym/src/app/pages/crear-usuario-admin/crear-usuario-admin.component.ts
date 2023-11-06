import { Component, OnInit } from '@angular/core';
import { UsuariosService } from 'src/app/services/usuarios.service';
import { HttpClient } from '@angular/common/http';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { JwtHelperService } from '@auth0/angular-jwt';

@Component({
  selector: 'app-crear-usuario-admin',
  templateUrl: './crear-usuario-admin.component.html',
  styleUrls: ['./crear-usuario-admin.component.css']
})
export class CrearUsuarioAdminComponent implements OnInit {
  formData: any = {};
  succesMessage: string = '';
  userRol:string = '';


  constructor(
    private usuariosService: UsuariosService,
    private router: Router,
    private jwtHelper: JwtHelperService,
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
          this.succesMessage = 'Usuario creado correctamente';
          // this.succesMessage = 'Usuario actualizado con éxito';
        setTimeout(() => {
        this.succesMessage = '';
        this.router.navigate(['/usuarios']);
      }, 3000);
      



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
ngOnInit() {
  const token = localStorage.getItem('token');
  // this.succesMessage='Esperando validación de token por el ADMIN, mas tarde verá todas las funcionalidades...';
  if (token){ // Reemplaza 'tu_variable_token' con el nombre de tu variable local que contiene el token.
    const decodedToken = this.jwtHelper.decodeToken(token);
    this.userRol = decodedToken.rol;
    if (this.userRol === 'profesor'){
      this.formData.rol = 'alumno';
    }
}
}
}
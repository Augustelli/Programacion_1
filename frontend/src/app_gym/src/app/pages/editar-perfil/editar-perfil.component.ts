import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { JwtHelperService } from '@auth0/angular-jwt';
import { UsuariosService } from 'src/app/services/usuarios.service';

@Component({
  selector: 'app-editar-perfil',
  templateUrl: './editar-perfil.component.html',
  styleUrls: ['./editar-perfil.component.css']
})
export class EditarPerfilComponent implements OnInit {
  userDni:string = '';
  userData: any = {};
  updatedFields: any = {};
  userRol:string = '';
  successMessage: string = '';
  toHome() {
    window.location.href = '/home';
  }

  constructor(
    private router: Router,
    private jwtHelper: JwtHelperService,
    private usuariosService: UsuariosService
    ) {}
  routeToPay(){
    this.router.navigate(['/pay']);
  }
  ngOnInit() {
    const token = localStorage.getItem('token');

    if (token){ 
      const decodedToken = this.jwtHelper.decodeToken(token);
      this.userDni = decodedToken.id;
      console.log('DNI del usuario', this.userDni);
      this.userRol = decodedToken.rol;
 
   
    this.usuariosService.getUserData(this.userDni).subscribe(
      (data: any) => {
        this.userData = data.Usuario[0];
        console.log('Datos del usuario', this.userData);
        this.fillFormFields();
      },
      (error) => {
        console.error('Error al obtener los datos del usuario', error);
      }
    );
    }
  }


fillFormFields() {
  // Llena los campos del formulario con los datos del usuario
  const { nombre, apellido, fecha_nacimiento, dni, email, nombre_usuario,rol, contrasegna, contrasegna2 } = this.userData;
  document.getElementById('nombre')!.setAttribute('value', nombre);
  document.getElementById('apellido')!.setAttribute('value', apellido);
  // document.getElementById('birth')!.setAttribute('value', fecha_nacimiento);
  document.getElementById('dni')!.setAttribute('value', dni);
  document.getElementById('email')!.setAttribute('value', email);
  document.getElementById('username')!.setAttribute('value', nombre_usuario);
  document.getElementById('rol')!.setAttribute('value', rol);
  document.getElementById('contrasegna')!.setAttribute('value', contrasegna);
  document.getElementById('contrasegna2')!.setAttribute('value', contrasegna2);
}
fieldChanged(fieldName: string, newValue: any) {
  // Actualiza el campo modificado en el objeto updatedFields
  this.updatedFields[fieldName] = newValue;
}

updateUser() {
  if (this.userData.contrasegna !== this.userData.contrasegna2) {
    alert('Las contraseñas no coinciden');
    // Agrega lógica adicional si las contraseñas no coinciden, como mostrar un mensaje de error al usuario
    return;
  }
  
  // Elimina el campo 'contrasegna2' del objeto updatedFields antes de enviarlo al servicio
  delete this.updatedFields['contrasegna2'];
  // Realiza la solicitud PUT con this.updatedFields
  this.usuariosService.updateUserData(this.userDni, this.updatedFields).subscribe(
    (response) => {
      console.log('Usuario actualizado:', response);
      this.successMessage = 'Usuario actualizado con éxito';
      setTimeout(() => {
        this.successMessage = '';
        this.router.navigate(['/home']);
      }, 3000);
    },
    (error) => {
      console.error('Error al actualizar el usuario', error);
    }
  );
}

}


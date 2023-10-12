import { Component, OnInit } from '@angular/core';
import { Input } from '@angular/core';
import { Router } from '@angular/router';
import { UsuariosService } from 'src/app/services/usuarios.service';
import { HttpClient } from '@angular/common/http';
import { JwtHelperService } from '@auth0/angular-jwt';


@Component({
  selector: 'app-abm',
  templateUrl: './abm.component.html',
  styleUrls: ['./abm.component.css']
})
export class AbmComponent implements OnInit {
  @Input() user_id!: string;
  @Input() tipoOperacion!: string;
  userData: any = {};
  updatedFields: any = {};
  successMessage: string = '';
  userRol:string = '';


  constructor(
    private router: Router,
    private usuariosService: UsuariosService,
    private http: HttpClient,
    private jwtHelper: JwtHelperService
    ) {}

  
    ngOnInit() {
      const token = localStorage.getItem('token');
      
      if (token){ // Reemplaza 'tu_variable_token' con el nombre de tu variable local que contiene el token.
        const decodedToken = this.jwtHelper.decodeToken(token);
        this.userRol = decodedToken.rol;
      }
    if (this.user_id) {
      // Utiliza el servicio para obtener los datos del usuario
      this.usuariosService.getUserData(this.user_id).subscribe(
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

//   ngOnInit() {
//     const token = localStorage.getItem('token');
//     this.successMessage='Esperando validación de token por el ADMIN, mas tarde verá todas las funcionalidades...';
//     if (token){ // Reemplaza 'tu_variable_token' con el nombre de tu variable local que contiene el token.
//       const decodedToken = this.jwtHelper.decodeToken(token);
//       this.userRol = decodedToken.rol;
//       this.isToken = true;
//   }else{
//     this.isToken = false;
    
//     this.successMessage='Usted no se ha registrado, la visión sera reducidada...';
//   }
// }

fillFormFields() {
  // Llena los campos del formulario con los datos del usuario
  const { nombre, apellido, fecha_nacimiento, dni, email, nombre_usuario,rol } = this.userData;
  document.getElementById('nombre')!.setAttribute('value', nombre);
  document.getElementById('apellido')!.setAttribute('value', apellido);
  // document.getElementById('birth')!.setAttribute('value', fecha_nacimiento);
  document.getElementById('dni')!.setAttribute('value', dni);
  document.getElementById('email')!.setAttribute('value', email);
  document.getElementById('username')!.setAttribute('value', nombre_usuario);
  document.getElementById('rol')!.setAttribute('value', rol);
}
back() {
  this.router.navigate(['/usuarios']);
}
fieldChanged(fieldName: string, newValue: any) {
  // Actualiza el campo modificado en el objeto updatedFields
  this.updatedFields[fieldName] = newValue;
}





updateUser() {
  // Realiza la solicitud PUT con this.updatedFields
  this.usuariosService.updateUserData(this.user_id, this.updatedFields).subscribe(
    (response) => {
      console.log('Usuario actualizado:', response);
      this.successMessage = 'Usuario actualizado con éxito';
      setTimeout(() => {
        this.successMessage = '';
        this.router.navigate(['/usuarios']);
      }, 3000);
    },
    (error) => {
      console.error('Error al actualizar el usuario', error);
    }
  );
}


}





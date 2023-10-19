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
  updatedFields2: any = {};
  updatedFields3: any = {};
  successMessage: string = '';
  userRol:string = '';
  userData1: any = {};
  userData2: any = {};
  userID: any = {};


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

    if (this.userRol) {
      // Utiliza el servicio para obtener los datos del usuario
      this.usuariosService.getUserData(this.user_id).subscribe(
        (data: any) => {
          this.userID = data.Usuario[0].dni;
          this.userData = data.Usuario[0];
          // console.log('Datos del usuario', this.userData);
          this.fillFormFields();
          if (this.userData.rol == 'profesor'){
            this.usuariosService.getUserDataProfesor(this.user_id).subscribe(
              (data: any) => {
                this.userData2 = data.Usuario[0];
                // console.log('Datos del profesor', this.userData2);
                // console.log('Datos del profesor', this.userData2);
                this.fillFormFields();
              },
              (error) => {
                console.error('Error al obtener los datos del usuario', error);
              }
            );
          }
          if (this.userData.rol == 'alumno'){
            this.usuariosService.getUserDataAlumno(this.user_id).subscribe(
              (data: any) => {
                // console.log('Datos del alumno', data);
                this.userData1 = data.Usuario[0];
                // console.log('Datos del alumno', this.userData1);
                this.fillFormFields();
              },
              (error) => {
                console.error('Error al obtener los datos del usuario', error);
              }
            );
          }
        },
        (error) => {
          console.error('Error al obtener los datos del usuario', error);
        }
      );
    }
  }


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
fieldChanged2(fieldName: string, newValue: any) {
  // Actualiza el campo modificado en el objeto updatedFields
  this.updatedFields2[fieldName] = newValue;
}
fieldChanged3(fieldName: string, newValue: any) {
  // Actualiza el campo modificado en el objeto updatedFields
  this.updatedFields3[fieldName] = newValue;
}







updateUser() {
  if (this.userData.rol === 'profesor') {
    this.usuariosService.updateUserDataProfesor(this.user_id, this.updatedFields3).subscribe(
      (response) => {
        // Manejar la respuesta del backend si es necesario
        console.log('Datos Profesor actualizados', response);
      },
      (error) => {
        console.error('Error al actualizar los datos', error);
      }
    );
  }


  if (this.userData1.rol === 'alumno') {
    // if (this.updatedFields['dni']) {
    //   this.updatedFields2['dni'] = parseFloat(this.updatedFields['dni']);
      
    // }
    
    console.log('UserData1', this.userData1);

    console.log('updatedfields del alumno', this.updatedFields2);
    console.log('userid', this.user_id);
    console.log('userid', this.userID);
    // Crear un objeto con los datos actualizados
  

    // Realizar la solicitud PUT al endpoint correspondiente
    this.usuariosService.updateUserDataAlumno(this.userID, this.updatedFields2).subscribe(
      (response) => {
        // Manejar la respuesta del backend si es necesario
        console.log('Datos actualizados', response);
      },
      (error) => {
        console.error('Error al actualizar los datos', error);
      }
    );
  }
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
  // if (this.userRol === 'alumno') {
    // Crear un objeto con los datos actualizados
   
     
}
// updateUserDataAlumno() {
  //   if (this.userRol === 'alumno') {
  //   // Crear un objeto con los datos actualizados
  //   const updatedData = {
  //     altura: this.userData1.altura,
  //     peso: this.userData1.peso,
  //   };

  //   // Realizar la solicitud PUT al endpoint correspondiente
  //   this.usuariosService.updateUserDataAlumno(this.user_id, updatedData).subscribe(
  //     (response) => {
  //       // Manejar la respuesta del backend si es necesario
  //       console.log('Datos actualizados', response);
  //     },
  //     (error) => {
  //       console.error('Error al actualizar los datos', error);
  //     }
  //   );
  // }

}






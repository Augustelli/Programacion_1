import { Component , OnInit} from '@angular/core';
import { JwtHelperService } from '@auth0/angular-jwt';

@Component({
  selector: 'app-ver-clases',
  templateUrl: './ver-clases.component.html',
  styleUrls: ['./ver-clases.component.css']
})
export class VerClasesComponent implements OnInit{

  varVerClases = true;
  isToken: boolean = false;
  userRol:string = '';
  dni: string = '';
  arrayClases: any;

  arrayClasesGuess=[
    {
      img:"../../../assets/clases/clases.png",
      nombreClase: "Entrenamiento Pecho",
      nombreProfesor: "Augusto Mancuso",
      horario: "Lunes 18:00hs",
      duracion: "1:00hs",
      cupos: "20"},

    {
      img:"../../../assets/clases/clases.png",
      nombreClase: "Entrenamiento Piernas",
      nombreProfesor: "Franco Narvaez",
      horario: "Martes 18:00hs",
      duracion: "1:00hs",
      cupos: "20"},
    {
      img:"../../../assets/clases/clases.png",
      nombreClase: "Zumba",
      nombreProfesor: "Juan Perez",
      horario: "Miercoles 18:00hs",
      duracion: "1:00hs",
      cupos: "20"},
    {
      img:"../../../assets/clases/clases.png",
      nombreClase: "Entrenamiento Pecho",
      nombreProfesor: "Augusto Mancuso",
      horario: "Jueves 18:00hs",
      duracion: "1:00hs",
      cupos: "20"},
    {
      img:"../../../assets/clases/clases.png",
      nombreClase: "Entrenamiento Piernas",
      nombreProfesor: "Franco Narvaez",
      horario: "Viernes 18:00hs",
      duracion: "1:00hs",
      cupos: "20"}


  ]
  getClasesEnPares() {
    const clasesEnPares = [];
    for (let i = 0; i < this.arrayClases.length; i += 2) {
      const par = [this.arrayClases[i], this.arrayClases[i + 1]];
      clasesEnPares.push(par);
    }
    return clasesEnPares;
  }

  constructor(
    private jwtHelper: JwtHelperService,
  ) { }

  ngOnInit(): void {
   
    
    const token = localStorage.getItem('token');
    // this.successMessage='Esperando validación de token por el ADMIN, mas tarde verá todas las funcionalidades...';
    if (token){ // Reemplaza 'tu_variable_token' con el nombre de tu variable local que contiene el token.
      const decodedToken = this.jwtHelper.decodeToken(token);
      this.userRol = decodedToken.rol;
      
      console.log('decodedToken', decodedToken.id);
      this.isToken = true;
      this.dni = decodedToken.id;
  }else{
    this.isToken = false;
    this.arrayClases = this.arrayClasesGuess;
  }
//   if (this.userRol=='profesor' || this.userRol=='admin')  {
//     // Utiliza el servicio para obtener los datos del usuario
//     this.planificacionService.getPlanificaciones().subscribe(
//       (data: any) => {
//         console.log('Datos del usuario', data);
//         this.arrayPlanificaciones = data.Planificacion;
//         // console.log('Datos del usuario', this.userData);
//         // this.fillFormFields();
//       },
//       (error) => {
//         console.error('Error al obtener los datos del usuario', error);
//       }
//     );
//   }
//   if(this.userRol=='alumno'){
//     this.planificacionService.getPlanificacionAlumno(this.dni).subscribe(
//       (data: any) => {
//         console.log('Datos del usuario', data);
//         this.arrayPlanificaciones = data.Planificacion;
//         // console.log('Datos del usuario', this.userData);
//         // this.fillFormFields();
//       },
//       (error) => {
//         console.error('Error al obtener los datos del usuario', error);
//       }
//     );
//   }
//   if(this.userRol=='espera'){
//     this.arrayPlanificaciones = this.arrayPlanificacionesGuess;
//   }
// }

  }
  
  verClases(){
      this.varVerClases = true;
    }

  ocultarClases(){
      this.varVerClases = false;}



}

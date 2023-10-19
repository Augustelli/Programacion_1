import { Component , OnInit} from '@angular/core';
import { Router } from '@angular/router';
import { JwtHelperService } from '@auth0/angular-jwt';
import { PagosService } from 'src/app/services/pagos.service';
import { UsuariosService } from 'src/app/services/usuarios.service';
import { ClasesService } from 'src/app/services/clases.service';

@Component({
  selector: 'app-profes',
  templateUrl: './profes.component.html',
  styleUrls: ['./profes.component.css']
})
export class ProfesComponent implements OnInit {

  constructor(
    private jwtHelper: JwtHelperService,
    private usuariosService: UsuariosService,
    private pagoService: PagosService,
    private router: Router,
    private clasesService: ClasesService
  ) { }

  arrayUsuarios: any;
  userRol:string = '';
  searchTerm: string = '';
  arrayClases: any;
  indice :any;
  mostrarFormularioCreacion = false;
  nuevaClaseProfe:any = {
    idProfesor:'',
    idClase:''}
  eliminarClaseProfe:any = {
    idProfesor:'',
    idClase:''}

  mostrarFormularioEliminacion = false;


  

  ngOnInit(): void {
    this.usuariosService.getProfes1().subscribe((data:any) => {
      this.arrayUsuarios = data.Usuario
      console.log('profes',this.arrayUsuarios);
    });
    
    const token = localStorage.getItem('token');
    if (token){ // Reemplaza 'tu_variable_token' con el nombre de tu variable local que contiene el token.
      const decodedToken = this.jwtHelper.decodeToken(token);
      this.userRol = decodedToken.rol;
    } 
    
}


  filtrarUsuariosNombre(){
    if (!this.searchTerm) {
      this.mostrarTodo();
      return;
    }
    this.arrayUsuarios = this.arrayUsuarios.filter((usuario: any) => {
      const nombreCompleto = `${usuario.nombre} ${usuario.apellido}${usuario.dni}`;
      return nombreCompleto.toLowerCase().includes(this.searchTerm.toLowerCase());
    });  
  }
  mostrarTodo(){
  this.usuariosService.getProfes1().subscribe((data: any) => {
    this.arrayUsuarios = data.Usuario
  });
}
mostrarInformacion(idProfesor: string, i: number) {
  this.clasesService.getClaseByProfesor(idProfesor).subscribe((data: any) => {
    console.log('Información de clase:', data);
    this.arrayClases = data;
    console.log('thisarrayclases',this.arrayClases);

   
    
    this.indice = i;
    console.log(this.indice);

  });
}

// const datosParaPost = {
//   dni: this.nuevopago.dni,
//   fecha_de_pago: this.nuevopago.fecha_de_pago,
//   monto: this.nuevopago.monto,
//   estado: this.nuevopago.estado
 
// };
// console.log('datosParaPost', datosParaPost);
// this.pagoService.crearPago(datosParaPost).subscribe((data: any) => {
//   console.log('Pago creado:', data);
//   this.mostrarFormularioCreacion = false;
  
// });
// }
crearProfeClase(){
  const datosParaPost = {
    idProfesor: this.nuevaClaseProfe.idProfesor,
    idClase: this.nuevaClaseProfe.idClase
  };
  console.log('datosParaPost', datosParaPost);
  this.clasesService.updateProfesorEnClase(datosParaPost).subscribe((data: any) => {
    console.log('Clase creada:', data);
    this.mostrarFormularioCreacion = false;
    
  });
  }
  getKeys(obj: any): string[] {
    return Object.keys(obj);
  }

  eliminarProfeYClase(){
    const datosParaDelete = {
      idProfesor: this.eliminarClaseProfe.idProfesor,
      idClase: this.nuevaClaseProfe.idClase
    };
    console.log('datosParaDelete', datosParaDelete);
    this.clasesService.deleteProfesorEnClase(datosParaDelete).subscribe((data: any) => {
      console.log('Clase eliminada:', data);
      this.mostrarFormularioEliminacion = false;
      
    });
  }
  eliminarProfe(idProfesor: string) {
    this.usuariosService.deleteProfesor(idProfesor).subscribe((data: any) => {
      console.log('Profesor eliminado:', data);
      this.mostrarTodo();
    });
  }
}






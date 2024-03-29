import { Component,OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { JwtHelperService } from '@auth0/angular-jwt';
import { PagosService } from 'src/app/services/pagos.service';
import { UsuariosService } from 'src/app/services/usuarios.service';

@Component({
  selector: 'app-pay-admin',
  templateUrl: './pay-admin.component.html',
  styleUrls: ['./pay-admin.component.css']
})
export class PayAdminComponent implements OnInit{
  constructor(
    private jwtHelper: JwtHelperService,
    private usuariosService: UsuariosService,
    private pagoService: PagosService,    
    private router: Router
  ){}

  page=1;
  perPage=4;
  isLastPage: boolean = true;
  totalItems = 0;
  estadoBoton = 1;
  estado : string = '';
  state : string = '';
  


  arrayUsuarios: any;
  userRol:string = '';
  searchTerm: string = '';
  arrayPagos: any;
  mostrarInfo: boolean = false;
  mostrarFormularioCreacion = false;
  arrayUsuariosIGNORE :any;
  mostrarFormularioEditar = false;

  nuevopago: any = {
    dni: '',
    fecha_de_pago: '',
    monto: '',
    estado: ''
  };

  ngOnInit(): void {
    this.estado = 'todos';
    this.page = 1;
    this.usuariosService.getUsers(this.page, this.perPage).subscribe((data1:any) => {
    })


    
    const token = localStorage.getItem('token');
    if (token){
      const decodedToken = this.jwtHelper.decodeToken(token);
      this.userRol = decodedToken.rol;
    }
    this.usuariosService.getAlumnos(this.page,this.perPage).subscribe((data:any) => {
      console.log('JSON data:', data);
      this.arrayUsuarios = data.Usuario;
      this.totalItems = data.Total;
      this.isLastPage = this.totalItems / this.perPage <= this.page;
    
      
    })
    
  }


  filtrarUsuariosNombre(){
    if (!this.searchTerm || this.searchTerm === '') {
      this.mostrarTodo();
      return;
    }
    const page=1;
    const perPage=1000;
    this.usuariosService.getAlumnos(page, perPage).subscribe((data:any) => {
      this.arrayUsuariosIGNORE = data.Usuario;
    })
    this.arrayUsuarios = this.arrayUsuariosIGNORE.filter((usuario: any) => {
      const nombreCompleto = `${usuario.nombre} ${usuario.apellido}${usuario.dni}`;
      return nombreCompleto.toLowerCase().includes(this.searchTerm.toLowerCase());
    });  
  }
  mostrarTodo() {
    this.estado='todos';
    this.ngOnInit();

  }
  mostrarDeuda(){
    this.estado='deuda';
    this.state = 'false';
    this.page=1;
    this.estadoBoton=2;

    console.log('paso por aqui,',this.state)
    this.usuariosService.getAlumnos1(this.page, this.perPage, this.state).subscribe(
      (data: any) => {
        console.log('JSON data:', data);
        this.arrayUsuarios = data.Usuario;
        this.totalItems = data.Total;
        this.isLastPage = this.totalItems / this.perPage <= this.page;
      },
      (error) => {
        console.error('Error al obtener datos de alumnos:', error);
        // Agrega el manejo de errores aquí, como mostrar un mensaje de error al usuario
      }
    );
  }

  mostarAlDia() {
    this.state = 'true';
    this.estado='alDia';
    this.estadoBoton=3;
    this.page=1;
    this.usuariosService.getAlumnos1(this.page, this.perPage, this.state).subscribe(
      (data: any) => {
        console.log('JSON data:', data);
        this.arrayUsuarios = data.Usuario;
        this.totalItems = data.Total;
        this.isLastPage = this.totalItems / this.perPage <= this.page;
      },
      // this.page=1;
      (error) => {
        console.error('Error al obtener datos de alumnos:', error);
        // Agrega el manejo de errores aquí, como mostrar un mensaje de error al usuario
      }
    );
  }
  


  mostrarInformacion(dni: string) {
    // Realiza las operaciones necesarias para obtener la información de pago del usuario
    this.pagoService.getPagosByDni(dni).subscribe((data: any) => {
      console.log('Información de pago:', data);
      console.log('Información de pago:', data.Pagos);
      this.arrayPagos = data.Pagos;
    
      const usuario = this.arrayUsuarios.find((usuario: any) => usuario.dni === dni);
      usuario.pagos = Object.values(data.Pagos);

      console.log('Usuario:', usuario);
      usuario.mostrandoPagos = true; // Establece la bandera mostrandoPagos en true para mostrar los detalles de pago

       // Asigna la información de pago al usuario específico
    });
  
    
  }
  
  ocultarPagos(usuario: any) {
    usuario.mostrandoPagos = false; // Establece la bandera mostrandoPagos en false para ocultar los detalles de pago
  }

  nuevoPago() {
    this.mostrarFormularioCreacion = true;
  }

  crearPago() {
    const fechaFormateada = this.formatoFecha(this.nuevopago.fecha_de_pago);
    if (!/^\d{8}$/.test(this.nuevopago.dni)) {
      console.error('El DNI debe tener exactamente 8 números');
      alert('El DNI debe tener exactamente 8 números');
      
      return;
    }
  
   
    if (!/^\d+(\.\d+)?$/.test(this.nuevopago.monto)) {
      console.error('El monto debe ser un número válido');
      alert('El monto debe ser un número válido');
    
      return;
    }
    const  estadix = "True"

    const datosParaPost = {
      dni: this.nuevopago.dni,
      fecha_de_pago: fechaFormateada,
      monto: this.nuevopago.monto,
      estado: estadix
     
    };
    console.log('datosParaPost', datosParaPost);
    this.pagoService.crearPago(datosParaPost).subscribe((data: any) => {
      console.log('Pago creado:', data);
      this.mostrarFormularioCreacion = false;
      this.ngOnInit();
      
    });
   

  }

  formatoFecha(fecha: any) {
    const partes = fecha.split('-');
    const fechaFormateada = `${partes[2]}/${partes[1]}/${partes[0]}`;
    return fechaFormateada;
  }

  deletePago(dni: string) {
    this.pagoService.deletePago(Number(dni))
      .subscribe(
        (response) => {
          // Assuming status code 0 indicates successful deletion
          alert('Pago eliminado con éxito');
          this.ngOnInit();
        }
      );
       // Perform any other necessary operations after successful deletion
       
  }

  modificarPago(usuario: any) {
    this.mostrarFormularioEditar=true;
    usuario.mostrandoPagos = false;
    usuario.editando = true
     // Establece la bandera mostrandoPagos en false para ocultar los detalles de pago


    
    
  }
 

  guardarCambios(usuario: any) {
    // Realiza las operaciones necesarias para guardar los cambios en la información de pago
    const pago = usuario.pagos[0];
    const datosParaPost = {
      dni: pago.dni,
      fecha_de_pago: pago.fecha_de_pago,
      monto: pago.monto,
      estado: pago.estado
    };

    console.log('datosParaPost', datosParaPost);
    this.pagoService.putPago(pago.idPago ,datosParaPost).subscribe((data: any) => {
      console.log('Pago creado:', data);
      usuario.editando = false; // Establece la bandera editando en false para ocultar el formulario de edición
      this.ngOnInit();
      
      
    }
    );


  }
  onClickAnteriorPag(){
    this.page-=1;
   
    if(this.estado === 'deuda'){
      this.state = 'false';
      }
    if(this.estado==='alDia'){
      this.state = 'true';
      }
    if(this.estado==='todos'){
      this.state = '';
      }
      
      console.log('paso por aqui: ', this.state)
      this.usuariosService.getAlumnos1(this.page, this.perPage, this.state).subscribe(
        (data: any) => {
          console.log('JSON data:', data);
          this.arrayUsuarios = data.Usuario;
          this.totalItems = data.Total;
          this.isLastPage = this.totalItems / this.perPage <= this.page;
        },
        (error) => {
          console.error('Error al obtener datos de alumnos:', error);
        }
      );
    
    


  }
onClickSiguientePag(){

  this.page+=1;
  

  if(this.estado === 'deuda'){
    this.state = 'false';
    }
  if(this.estado==='alDia'){
    this.state = 'true';
    }
  if(this.estado==='Todos'){
    this.state = '';
    }
    
    console.log('paso por aqui: ', this.state)
    this.usuariosService.getAlumnos1(this.page, this.perPage, this.state).subscribe(
      (data: any) => {
        console.log('JSON data:', data);
        this.arrayUsuarios = data.Usuario;
        this.totalItems = data.Total;
        this.isLastPage = this.totalItems / this.perPage <= this.page;
      },
      (error) => {
        console.error('Error al obtener datos de alumnos:', error);
      }
    );
  }

}

  



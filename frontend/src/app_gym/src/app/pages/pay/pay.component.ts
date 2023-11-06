import { Component , OnInit} from '@angular/core';
import { PagosService } from '../../services/pagos.service';
import { JwtHelperService } from '@auth0/angular-jwt';
import { DatePipe } from '@angular/common';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';





@Component({
  selector: 'app-pay',
  templateUrl: './pay.component.html',
  styleUrls: ['./pay.component.css']
})
export class PayComponent implements OnInit{

  monto: number = 9.99;
  seleccion:string = 'monthly';
  userRol:string = '';
  isToken: boolean = false;
  userDni: string = '';

  constructor(
    private pagosService: PagosService,
    private jwtHelper: JwtHelperService,
    private router: Router,
    private toastr: ToastrService

  ) { }

  ngOnInit():void{
    const token = localStorage.getItem('token');
    if (token){ // Reemplaza 'tu_variable_token' con el nombre de tu variable local que contiene el token.
      const decodedToken = this.jwtHelper.decodeToken(token);
      this.userRol = decodedToken.rol;
      this.isToken = true;
      this.userDni = decodedToken.id;

  }else{
    this.isToken = false;
    
  }
  }

  realizarPago(){
    let fechaActual = new Date();


    if (this.seleccion === 'monthly') {
     
      fechaActual.setMonth(fechaActual.getMonth() + 1);
    } else if (this.seleccion === 'yearly') {
      
      fechaActual.setFullYear(fechaActual.getFullYear() + 1);
    }
  
    
    let datePipe = new DatePipe('en-US');
    let fechaFormateada = datePipe.transform(fechaActual, 'dd/MM/yyyy');

    let pago = {
      monto: this.monto,
      // seleccion: this.seleccion,
      fecha_de_pago: fechaFormateada,
      estado : 'pagado',
      dni: this.userDni

    }

    console.log(pago);


    this.pagosService.realizarPago(pago).subscribe(
      (res) => {
        console.log(res);
        alert('Pago realizado con éxito');
        this.router.navigate(['/home']);
      },
      (err) => {
        alert('Hubo un error al procesar el pago');
      }
    )
       
     
  }
  
  



}

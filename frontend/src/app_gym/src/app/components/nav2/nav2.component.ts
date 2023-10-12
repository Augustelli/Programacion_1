import { Component , OnInit} from '@angular/core';
import { Router } from '@angular/router';
import { JwtHelperService } from '@auth0/angular-jwt';

@Component({
  selector: 'app-nav2',
  templateUrl: './nav2.component.html',
  styleUrls: ['./nav2.component.css']
})
export class Nav2Component  implements OnInit{
  // rolUsuario = 'admin';
  userRol:string = '';

  constructor(
    private router: Router,
    private jwtHelper: JwtHelperService
    ) {}
  
  get isToken() {
    return !!localStorage.getItem('token');
  }

  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token){ // Reemplaza 'tu_variable_token' con el nombre de tu variable local que contiene el token.
      const decodedToken = this.jwtHelper.decodeToken(token);
      this.userRol = decodedToken.rol;
  }
}


  
    
  redirectLogout() {
    this.router.navigate(['/logout']);
  }


  redirectEditar() {
    this.router.navigate(['/editar_perfil']);
  }

  routeTrouteToAlumnoProfesorListado() {
    this.router.navigate(['/usuarios']);
  }
  redirectLogin() {
    this.router.navigate(['/login_two'], { queryParams: { varLogin: true } });
  }
  redirectSignIn() {
    this.router.navigate(['/login_two'], { queryParams: { varLogin: false } });
  }
  
}
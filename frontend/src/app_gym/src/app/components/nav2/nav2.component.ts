import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-nav2',
  templateUrl: './nav2.component.html',
  styleUrls: ['./nav2.component.css']
})
export class Nav2Component {
  rolUsuario = 'admin';

  constructor(private router: Router) {}

  redirectLogout() {
    this.router.navigate(['/logout']);
  }

  redirectEditar() {
    this.router.navigate(['/editar_perfil']);
  }

  routeTrouteToAlumnoProfesorListado() {
    this.router.navigate(['/usuarios']);
  }
}
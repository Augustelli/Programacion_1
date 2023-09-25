import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-editar-perfil',
  templateUrl: './editar-perfil.component.html',
  styleUrls: ['./editar-perfil.component.css']
})
export class EditarPerfilComponent {
  toHome() {
    window.location.href = '/home';
  }

  constructor(private router: Router) {}
  routeToPay(){
    this.router.navigate(['/pay']);
  }
}

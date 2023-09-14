import { Component } from '@angular/core';
import { TablaPlanificacionGrillaaComponent } from 'src/app/components/tabla-planificacion-grillaa/tabla-planificacion-grillaa.component';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  varVerPlanificaciones = true;
  varNoVerPlanificaciones = false;

  onPlanificacionClickeada() {
    this.varVerPlanificaciones = false;
    this.varNoVerPlanificaciones = true; // Cambia esto según tu lógica
  }
  back() {
    this.varVerPlanificaciones = true;
    this.varNoVerPlanificaciones = false;
  }

}

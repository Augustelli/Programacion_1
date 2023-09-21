import { AfterViewInit, Component } from '@angular/core';
import { ViewChild } from '@angular/core';
import {MatPaginator, MatPaginatorModule} from '@angular/material/paginator';
import {MatTableDataSource, MatTableModule} from '@angular/material/table';;
import { NgIf,NgFor } from '@angular/common';

@Component({
  selector: 'app-tabla-planificacion-grillaa',
  templateUrl: './tabla-planificacion-grillaa.component.html',
  styleUrls: ['./tabla-planificacion-grillaa.component.css'],
  standalone: true,
  imports: [MatTableModule, NgIf, NgFor],



})
export class TablaPlanificacionGrillaaComponent implements AfterViewInit {
  displayedColumns: string[] = ['position', 'name', 'weight', 'symbol'];
  dataSource = new MatTableDataSource<PeriodicElement>(ELEMENT_DATA);
  clickedRows = new Set<PeriodicElement>();

  @ViewChild(MatPaginator)
  paginator!: MatPaginator;
  currentDay = 1;

  ngAfterViewInit() {
    this.dataSource.paginator = this.paginator;
    // this.changeDay(1);
  }

  changeDay(delta: number) {
    // Actualiza el día actual sumando o restando delta
    this.currentDay += delta;
  
    // Asegúrate de que el día actual esté dentro del rango deseado (en tu caso, del 1 al 6)
    if (this.currentDay < 1) {
      this.currentDay = 1;
    } else if (this.currentDay > 6) {
      this.currentDay = 6;
    }

  
    // Actualiza los datos de la tabla según el nuevo día seleccionado
    this.dataSource.data = ELEMENT_DATA.filter((element) => element.day === this.currentDay);
  }
  // changeDay(newDay: number) {
  //   this.dataSource.data = ELEMENT_DATA.filter((element) => element.day === newDay);
  // }
  onDaySelectChange(event: any) {
    const selectedDay = event?.target?.value; // Accede a value de manera segura
    if (selectedDay !== undefined) {
      // Realiza alguna acción con el día seleccionado, por ejemplo, filtrar los datos
      this.changeDay(parseInt(selectedDay, 10)); // Convierte el valor a número
    
    }
  }
}
// const maxDay: number = 3;
//   changeDay(delta: number) {
//     this.currentDay += delta;
//     if (this.currentDay < 1) {
//       this.currentDay = 1;
//     } else if (this.currentDay > maxDay) {
//       this.currentDay = maxDay; // Define el número máximo de días si es necesario
//     }
//     this.dataSource.data = ELEMENT_DATA.filter((element) => element.day === this.currentDay);
//   }



export interface PeriodicElement {
  name: string;
  position: number;
  weight: number;
  // symbol: string;
  repetition: number;
  day:number;
}

// const ELEMENT_DATA: PeriodicElement[] = [


//     // Filas para el día 1
//     { position: 1, name: 'Biceps', weight: 20, repetition:3, day: 1 },
//     { position: 2, name: 'Triceps', weight: 45, repetition:5 , day: 1 },

// ];
   
const ELEMENT_DATA: PeriodicElement[] = [
  // Filas para el día 1
  { position: 1, name: 'Biceps', weight: 20, repetition: 3, day: 1 },
  { position: 2, name: 'Triceps', weight: 45, repetition: 5, day: 1 },

  // Filas para el día 2
  { position: 3, name: 'Pecho', weight: 30, repetition: 4, day: 2 },
  { position: 4, name: 'Espalda', weight: 40, repetition: 5, day: 2 },

  // Filas para el día 3
  { position: 5, name: 'Piernas', weight: 50, repetition: 6, day: 3 },
  { position: 6, name: 'Hombros', weight: 25, repetition: 4, day: 3 },

  // Filas para el día 4
  { position: 7, name: 'Abdominales', weight: 10, repetition: 3, day: 4 },
  { position: 8, name: 'Cardio', weight: 0, repetition: 0, day: 4 },

  // Filas para el día 5
  { position: 9, name: 'Descanso', weight: 0, repetition: 0, day: 5 },

  // Filas para el día 6
  { position: 10, name: 'Yoga', weight: 0, repetition: 0, day: 6 },
  { position: 11, name: 'Estiramientos', weight: 0, repetition: 0, day: 6 },
];




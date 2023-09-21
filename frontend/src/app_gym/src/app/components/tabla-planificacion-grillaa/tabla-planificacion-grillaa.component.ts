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

  
  changeDay(newDay: number) {
    this.dataSource.data = ELEMENT_DATA.filter((element) => element.day === newDay);
  }
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
  symbol: string;
  day:number;
}

const ELEMENT_DATA: PeriodicElement[] = [
  // {position: 1, name: 'Hydrogen', weight: 1.0079, symbol: 'H'},
  // {position: 2, name: 'Helium', weight: 4.0026, symbol: 'He'},
  // {position: 3, name: 'Lithium', weight: 6.941, symbol: 'Li'},
  // {position: 4, name: 'Beryllium', weight: 9.0122, symbol: 'Be'},
  // {position: 5, name: 'Boron', weight: 10.811, symbol: 'B'},
  // {position: 6, name: 'Carbon', weight: 12.0107, symbol: 'C'},
  // {position: 7, name: 'Nitrogen', weight: 14.0067, symbol: 'N'},
  // {position: 8, name: 'Oxygen', weight: 15.9994, symbol: 'O'},
  // {position: 9, name: 'Fluorine', weight: 18.9984, symbol: 'F'},
  // {position: 10, name: 'Neon', weight: 20.1797, symbol: 'Ne'},
  // {position: 11, name: 'Sodium', weight: 22.9897, symbol: 'Na'},
  // {position: 12, name: 'Magnesium', weight: 24.305, symbol: 'Mg'},
  // {position: 13, name: 'Aluminum', weight: 26.9815, symbol: 'Al'},
  // {position: 14, name: 'Silicon', weight: 28.0855, symbol: 'Si'},
  // {position: 15, name: 'Phosphorus', weight: 30.9738, symbol: 'P'},
  // {position: 16, name: 'Sulfur', weight: 32.065, symbol: 'S'},
  // {position: 17, name: 'Chlorine', weight: 35.453, symbol: 'Cl'},
  // {position: 18, name: 'Argon', weight: 39.948, symbol: 'Ar'},
  // {position: 19, name: 'Potassium', weight: 39.0983, symbol: 'K'},
  // {position: 20, name: 'Calcium', weight: 40.078, symbol: 'Ca'},

    // Filas para el día 1
    { position: 1, name: 'Hydrogen', weight: 1.0079, symbol: 'H', day: 1 },
    { position: 2, name: 'Helium', weight: 4.0026, symbol: 'He', day: 1 },
    // ... Otras filas para el día 1
  
    // Filas para el día 2
    { position: 21, name: 'Scandium', weight: 44.9559, symbol: 'Sc', day: 2 },
    { position: 22, name: 'Titanium', weight: 47.867, symbol: 'Ti', day: 2 },
    // ... Otras filas para el día 2
  
    // Filas para el día 3
    { position: 38, name: 'Strontium', weight: 87.62, symbol: 'Sr', day: 3 },
    { position: 39, name: 'Yttrium', weight: 88.90585, symbol: 'Y', day: 3 },
    // ... Otras filas para el día 3
  
    // Filas para el día 4
    { position: 55, name: 'Cesium', weight: 132.90545196, symbol: 'Cs', day: 4 },
    { position: 56, name: 'Barium', weight: 137.327, symbol: 'Ba', day: 4 },
    // ... Otras filas para el día 4
  
    // Filas para el día 5
    { position: 72, name: 'Hafnium', weight: 178.49, symbol: 'Hf', day: 5 },
    { position: 73, name: 'Tantalum', weight: 180.94788, symbol: 'Ta', day: 5 },
    // ... Otras filas para el día 5
  
    // Filas para el día 6
    { position: 89, name: 'Actinium', weight: 227, symbol: 'Ac', day: 6 },
    { position: 90, name: 'Thorium', weight: 232.03806, symbol: 'Th', day: 6 },
    // ... Otras filas para el día 6
  ];





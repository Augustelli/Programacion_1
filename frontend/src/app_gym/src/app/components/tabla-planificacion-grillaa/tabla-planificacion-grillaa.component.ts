// // import { AfterViewInit, Component } from '@angular/core';
// // import { ViewChild } from '@angular/core';
// // import {MatPaginator, MatPaginatorModule} from '@angular/material/paginator';
// // import {MatTableDataSource, MatTableModule} from '@angular/material/table';;
// // import { NgIf,NgFor } from '@angular/common';

// // @Component({
// //   selector: 'app-tabla-planificacion-grillaa',
// //   templateUrl: './tabla-planificacion-grillaa.component.html',
// //   styleUrls: ['./tabla-planificacion-grillaa.component.css'],
// //   standalone: true,
// //   imports: [MatTableModule, NgIf, NgFor],
 
  

// // })
// // export class TablaPlanificacionGrillaaComponent implements AfterViewInit {
//   // displayedColumns: string[] = ['position', 'name', 'weight', 'symbol'];
//   // displayedColumns: string[] = ['id', 'name', 'category', 'repetitions'];
//   // dataSource = new MatTableDataSource<PeriodicElement>(ELEMENT_DATA);
//   // clickedRows = new Set<PeriodicElement>();
// //   dataSource = new MatTableDataSource<Exercise>([]);
// //     currentDayIndex = 0;

// //   @ViewChild(MatPaginator)
// //   paginator!: MatPaginator;

// //   showNextDay() {

// //     if (this.currentDayIndex < exercisesByDay.length - 1) {
// //       this.currentDayIndex++;
// //       this.dataSource.data = exercisesByDay[this.currentDayIndex];
// //     }
// //   }
// //   showPrevDay() {
// //     if (this.currentDayIndex > 0) {
// //       this.currentDayIndex--;
// //       this.dataSource.data = exercisesByDay[this.currentDayIndex];
// //     }
// //   }


// //   ngAfterViewInit() {
// //     this.dataSource.paginator = this.paginator;
// //   }
// // }

// // export interface PeriodicElement {
// //   id: number;
// //   name: string;
// //   category: string;
// //   repetitions: string;
//   // position: number;
//   // name: string;
//   // weight: number;
//   // symbol: string;
// // }
// // export interface Exercise {
// //   id: number;
// //   name: string;
// //   category: string;
// //   repetitions: string;
//   // position: number;
//   // name: string;
//   // weight: number;
//   // symbol: string;
// // }

// // const ELEMENT_DATA: PeriodicElement[] = [
// //   {position: 1, name: 'Hydrogen', weight: 1.0079, symbol: 'H'},
// //   {position: 2, name: 'Helium', weight: 4.0026, symbol: 'He'},
// //   {position: 3, name: 'Lithium', weight: 6.941, symbol: 'Li'},
// //   {position: 4, name: 'Beryllium', weight: 9.0122, symbol: 'Be'},
// //   {position: 5, name: 'Boron', weight: 10.811, symbol: 'B'},
// //   {position: 6, name: 'Carbon', weight: 12.0107, symbol: 'C'},
// //   {position: 7, name: 'Nitrogen', weight: 14.0067, symbol: 'N'},
// //   {position: 8, name: 'Oxygen', weight: 15.9994, symbol: 'O'},
// //   {position: 9, name: 'Fluorine', weight: 18.9984, symbol: 'F'},
// //   {position: 10, name: 'Neon', weight: 20.1797, symbol: 'Ne'},
// //   {position: 11, name: 'Sodium', weight: 22.9897, symbol: 'Na'},
// //   {position: 12, name: 'Magnesium', weight: 24.305, symbol: 'Mg'},
// //   {position: 13, name: 'Aluminum', weight: 26.9815, symbol: 'Al'},
// //   {position: 14, name: 'Silicon', weight: 28.0855, symbol: 'Si'},
// //   {position: 15, name: 'Phosphorus', weight: 30.9738, symbol: 'P'},
// //   {position: 16, name: 'Sulfur', weight: 32.065, symbol: 'S'},
// //   {position: 17, name: 'Chlorine', weight: 35.453, symbol: 'Cl'},
// //   {position: 18, name: 'Argon', weight: 39.948, symbol: 'Ar'},
// //   {position: 19, name: 'Potassium', weight: 39.0983, symbol: 'K'},
// //   {position: 20, name: 'Calcium', weight: 40.078, symbol: 'Ca'},
// // ];

// // const EXERCISE_DATA: Exercise[] = [
// //   const ELEMENT_DATA: PeriodicElement[] = [
// //   {id: 1, name: 'Push-up', category: 'Upper Body', repetitions: '3 sets of 15 reps'},
// //   {id: 2, name: 'Pull-up', category: 'Upper Body', repetitions: '3 sets of 10 reps'},
// //   {id: 3, name: 'Squat', category: 'Lower Body', repetitions: '4 sets of 12 reps'},
// //   {id: 4, name: 'Deadlift', category: 'Lower Body', repetitions: '4 sets of 8 reps'},
// //   {id: 5, name: 'Bench Press', category: 'Upper Body', repetitions: '3 sets of 10 reps'},
// //   {id: 6, name: 'Leg Press', category: 'Lower Body', repetitions: '4 sets of 12 reps'},
// //   {id: 7, name: 'Bicep Curl', category: 'Arm', repetitions: '3 sets of 12 reps'},
// //   {id: 8, name: 'Tricep Dip', category: 'Arm', repetitions: '3 sets of 12 reps'},
// //   {id: 9, name: 'Plank', category: 'Core', repetitions: '3 sets of 30 seconds'},
// //   {id: 10, name: 'Russian Twist', category: 'Core', repetitions: '3 sets of 20 reps'},
// //   {id: 11, name: 'Lunges', category: 'Lower Body', repetitions: '3 sets of 10 reps per leg'},
// //   {id: 12, name: 'Calf Raises', category: 'Lower Body', repetitions: '3 sets of 15 reps'},
// //   {id: 13, name: 'Lat Pulldown', category: 'Upper Body', repetitions: '3 sets of 12 reps'},
// //   {id: 14, name: 'Shoulder Press', category: 'Upper Body', repetitions: '3 sets of 10 reps'},
// //   {id: 15, name: 'Hanging Leg Raise', category: 'Core', repetitions: '3 sets of 12 reps'},
// //   {id: 16, name: 'Hamstring Curl', category: 'Lower Body', repetitions: '3 sets of 12 reps'},
// //   {id: 17, name: 'Side Plank', category: 'Core', repetitions: '3 sets of 30 seconds per side'},
// //   {id: 18, name: 'Barbell Rows', category: 'Upper Body', repetitions: '3 sets of 10 reps'},
// //   {id: 19, name: 'Dumbbell Flyes', category: 'Upper Body', repetitions: '3 sets of 12 reps'},
// //   {id: 20, name: 'Box Jumps', category: 'Lower Body', repetitions: '3 sets of 10 jumps'},
// // ];




// // const mondayExercises: Exercise[] = [
// //   {id: 1, name: 'Push-up', category: 'Upper Body', repetitions: '3 sets of 15 reps'},
// //   {id: 2, name: 'Pull-up', category: 'Upper Body', repetitions: '3 sets of 10 reps'},
// //   // ... otros ejercicios para el lunes
// // ];

// const tuesdayExercises: Exercise[] = [
//   {id: 4, name: 'Deadlift', category: 'Lower Body', repetitions: '4 sets of 8 reps'},
//   {id: 5, name: 'Bench Press', category: 'Upper Body', repetitions: '3 sets of 10 reps'},
//   {id: 6, name: 'Leg Press', category: 'Lower Body', repetitions: '4 sets of 12 reps'},
//   {id: 7, name: 'Bicep Curl', category: 'Arm', repetitions: '3 sets of 12 reps'},
//   {id: 8, name: 'Tricep Dip', category: 'Arm', repetitions: '3 sets of 12 reps'},
//   {id: 9, name: 'Plank', category: 'Core', repetitions: '3 sets of 30 seconds'},
//   // Ejercicios para el martes
// ];

// const wednesdayExercises: Exercise[] = [
//   {id: 12, name: 'Calf Raises', category: 'Lower Body', repetitions: '3 sets of 15 reps'},
//   {id: 13, name: 'Lat Pulldown', category: 'Upper Body', repetitions: '3 sets of 12 reps'},
//   {id: 14, name: 'Shoulder Press', category: 'Upper Body', repetitions: '3 sets of 10 reps'},
//   {id: 15, name: 'Hanging Leg Raise', category: 'Core', repetitions: '3 sets of 12 reps'},
//   {id: 16, name: 'Hamstring Curl', category: 'Lower Body', repetitions: '3 sets of 12 reps'},
//   {id: 17, name: 'Side Plank', category: 'Core', repetitions: '3 sets of 30 seconds per side'},
//   {id: 18, name: 'Barbell Rows', category: 'Upper Body', repetitions: '3 sets of 10 reps'},
//   {id: 19, name: 'Dumbbell Flyes', category: 'Upper Body', repetitions: '3 sets of 12 reps'},
//   {id: 20, name: 'Box Jumps', category: 'Lower Body', repetitions: '3 sets of 10 jumps'},
//   // Ejercicios para el miércoles
// ];

// // Define una matriz de ejercicios para cada día de la semana
// const exercisesByDay: Exercise[][] = [
//   mondayExercises,
//   tuesdayExercises,
//   wednesdayExercises,
//   // ... otros días de la semana
// ];

import { Component } from '@angular/core';

@Component({
  selector: 'app-tu-componente',
  templateUrl: './tu-componente.component.html',
  styleUrls: ['./tu-componente.component.css'],
})
export class TuComponenteComponent {
  displayedColumns: string[] = ['id', 'name', 'category', 'repetitions'];
  dataSource = new MatTableDataSource<Exercise>([]);

  currentDayIndex = 0; // Índice del día actual

  // Función para mostrar los ejercicios del día siguiente
  showNextDay() {
    if (this.currentDayIndex < exercisesByDay.length - 1) {
      this.currentDayIndex++;
      this.dataSource.data = exercisesByDay[this.currentDayIndex];
      this.updateDayLabel();
    }
  }

  // Función para mostrar los ejercicios del día anterior
  showPrevDay() {
    if (this.currentDayIndex > 0) {
      this.currentDayIndex--;
      this.dataSource.data = exercisesByDay[this.currentDayIndex];
      this.updateDayLabel();
    }
  }

  // Función para actualizar la etiqueta del día en tu HTML
  updateDayLabel() {
    const daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
    const currentDay = daysOfWeek[this.currentDayIndex];
    document.getElementById('dayLabel')!.textContent = `Nombre del Alumno<br>${currentDay}`;
  }
}

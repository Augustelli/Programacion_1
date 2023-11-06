// import { Component, Input } from '@angular/core';
// import { Output,EventEmitter } from '@angular/core';


// @Component({
//   selector: 'app-scroll-numbers',
//   template: `
//     <div class="day-selector">
//       <div class="day" *ngFor="let day of days" (click)="selectDay(day)">
//         <div class="day-name">{{ day.dayName }}</div>
//         <div class="day-number">{{ day.dayNumber }}</div>
//       </div>
//     </div>
//   `,
//   styles: [
//     `
//       .day-selector {
//         display: flex;
//         flex-direction: column;
//         overflow-y: scroll;
//         height: 200px;
//       }
//       .day {
//         display: flex;
//         flex-direction: column;
//         align-items: center;
//         justify-content: center;
//         height: 50px;
//         cursor: pointer;
//       }
//       .day:hover {
//         background-color: #f2f2f2;
//       }
//       .day-name {
//         font-size: 12px;
//         font-weight: bold;
//         text-transform: uppercase;
//       }
//       .day-number {
//         font-size: 24px;
//         font-weight: bold;
//       }
//     `,
//   ],
// })
// export class ScrollNumbersComponent {
//   days: { dayName: string; dayNumber: number }[] = [];

//   constructor() {
//     const today = new Date();
//     for (let i = 0; i < 7; i++) {
//       const date = new Date(today);
//       date.setDate(today.getDate() + i);
//       this.days.push({
//         dayName: date.toLocaleString('default', { weekday: 'short' }),
//         dayNumber: date.getDate(),
//       });
//     }
//   }

//   selectDay(day: { dayName: string; dayNumber: number }) {
//     console.log(`Selected ${day.dayName} ${day.dayNumber}`);
//   }
//   @Input() values: number[] = [];
//   activeIndex: number = 0;

//   onValueClick(index: number) {
//     this.activeIndex = index;
//   }
// }
import { Component, Input, Output, EventEmitter } from '@angular/core';
import { OnChanges,SimpleChanges } from '@angular/core';
import { Injectable } from '@angular/core';

@Component({
  selector: 'app-scroll-numbers',
  template: `
  <div class="day-selector">
    <div
      class="day"
      *ngFor="let day of days"
      (click)="selectDay(day.dayNumber)"
      [class.selected]="day.dayNumber === selectedNumber"
    >
      <div class="day-number">{{ day.dayNumber }}</div>
    </div>
  </div> `,

  styles: [
    `
      .day-selector {
        display: flex;
        flex-direction: column;
        overflow-y: scroll;
        height: 200px;
      }
      .selected {
        color:#1976D2;
        font-size: 36px;
      }
      .day {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 50px;
        cursor: pointer;
      }
      .day:hover {
        background-color: #f2f2f2;
      }
      .day-number {
        font-size: 24px;
        font-weight: bold;
      }
    `,
  ],
})
export class ScrollNumbersComponent implements OnChanges {
  @Input() minValue: number = 1; // Valor mínimo para el rango
  @Input() maxValue: number = 7; // Valor máximo para el rango
  @Output() daySelected = new EventEmitter<number>(); // Emitir el número seleccionado
  
  
  selectedNumber: number | null = null;
  contador:number = 0;

  days: { dayNumber: number }[] = [];
  ngOnChanges(changes: SimpleChanges) {
    // Detectar cambios en los valores de minValue o maxValue
    if (changes['minValue'] || changes['maxValue']) {
      // Regenerar los números dentro del nuevo rango especificado
      this.days = [];
      for (let i = this.minValue; i <= this.maxValue; i++) {
        this.days.push({
          dayNumber: i,
        });
      }
    }
  }

  


  constructor() {
    // Generar los números dentro del rango especificado
    for (let i = this.minValue; i <= this.maxValue; i++) {
      this.days.push({
        dayNumber: i,
      });
    }
  }

  // selectDay(dayNumber: number) {
  //   // Emitir el número seleccionado cuando se hace clic en un día
  //   this.daySelected.emit(dayNumber);
  //   this.selectedNumber = dayNumber;
  //   return dayNumber
  //   // localStorage.setItem('day', this.selectedNumber.toString());
  // }
  // guardarFecha(){
  //   localStorage.setItem('dia', this.selectedNumber.toString())
  //   localStorage.setItem('mes', this.selectedNumber.toString())
  //   localStorage.setItem('anio',this.selectedNumber.toString())
  // }

  
  selectDay(dayNumber: number) {
    // Emitir el número seleccionado cuando se hace clic en un día
    this.daySelected.emit(dayNumber);
    this.selectedNumber = dayNumber;
  
  //   if (!localStorage.getItem('dia')) {
  //     localStorage.setItem('dia', this.selectedNumber.toString());
  //   } else if (!localStorage.getItem('mes')) {
  //     localStorage.setItem('mes', this.selectedNumber.toString());
  //   } else if (!localStorage.getItem('anio')) {
  //     localStorage.setItem('anio', this.selectedNumber.toString());
  //   } else if (!localStorage.getItem('altura')) {
  //     localStorage.setItem('altura', this.selectedNumber.toString());
  //   } else if (!localStorage.getItem('peso')) {
  //     localStorage.setItem('peso', this.selectedNumber.toString());
  // }
  
//   if (this.variable === 0){
//     localStorage.setItem('dia', this.selectedNumber.toString());
//     this.contador = this.contador + 1;
// } else if (this.contador === 1){
//     localStorage.setItem('mes', this.selectedNumber.toString());
    
//   } else if (this.contador === 2){
//     localStorage.setItem('anio', this.selectedNumber.toString());
    
//   }else if (this.contador === 3){
//     localStorage.setItem('altura', this.selectedNumber.toString());
    
//   } else if (this.contador === 4){
//     localStorage.setItem('peso', this.selectedNumber.toString());
    
//   }

}

  
}


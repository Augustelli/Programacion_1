import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-scroll-numbers',
  template: `
    <div class="day-selector">
      <div class="day" *ngFor="let day of days" (click)="selectDay(day)">
        <div class="day-name">{{ day.dayName }}</div>
        <div class="day-number">{{ day.dayNumber }}</div>
      </div>
    </div>
  `,
  styles: [
    `
      .day-selector {
        display: flex;
        flex-direction: column;
        overflow-y: scroll;
        height: 200px;
      }
      .day {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 50px;
        cursor: pointer;
      }
      .day:hover {
        background-color: #f2f2f2;
      }
      .day-name {
        font-size: 12px;
        font-weight: bold;
        text-transform: uppercase;
      }
      .day-number {
        font-size: 24px;
        font-weight: bold;
      }
    `,
  ],
})
export class ScrollNumbersComponent {
  days: { dayName: string; dayNumber: number }[] = [];

  constructor() {
    const today = new Date();
    for (let i = 0; i < 7; i++) {
      const date = new Date(today);
      date.setDate(today.getDate() + i);
      this.days.push({
        dayName: date.toLocaleString('default', { weekday: 'short' }),
        dayNumber: date.getDate(),
      });
    }
  }

  selectDay(day: { dayName: string; dayNumber: number }) {
    console.log(`Selected ${day.dayName} ${day.dayNumber}`);
  }
  @Input() values: number[] = [];
  activeIndex: number = 0;

  onValueClick(index: number) {
    this.activeIndex = index;
  }
}

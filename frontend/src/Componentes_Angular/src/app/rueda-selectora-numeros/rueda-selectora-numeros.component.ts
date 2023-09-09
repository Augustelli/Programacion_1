import { Component } from '@angular/core';

@Component({
  selector: 'app-rueda-selector',
  templateUrl: './rueda-selector.component.html',
  styleUrls: ['./rueda-selector.component.css']
})
export class RuedaSelectorComponent {
  values: number[] = [];
  activeIndex: number = 0;

  constructor() {
    for (let i = 100; i <= 200; i++) {
      this.values.push(i);
    }

    this.activeIndex = this.values[0];
  }

  onWheel(event: WheelEvent) {
    if (event.deltaY > 0) {
      this.incrementActiveIndex();
    } else {
      this.decrementActiveIndex();
    }
  }

  incrementActiveIndex() {
    if (this.activeIndex < this.values[this.values.length - 1]) {
      this.activeIndex++;
    }
  }

  decrementActiveIndex() {
    if (this.activeIndex > this.values[0]) {
      this.activeIndex--;
    }
  }
}

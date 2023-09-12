import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-scroll-numbers',
  templateUrl: './scroll-numbers.component.html',
  styleUrls: ['./scroll-numbers.component.css']
})
export class ScrollNumbersComponent {
  @Input() values: number[] = [];
  activeIndex: number = 0;

  onValueClick(index: number) {
    this.activeIndex = index;
  }
}

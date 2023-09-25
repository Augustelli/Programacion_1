import { Component, EventEmitter, Output } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-botones-bkct',
  template: `
    <div class="col-sm-12 text-center" style="margin-top: 1rem; margin-bottom: 1rem;">
      <div class="row">
        <div class="d-flex justify-content-center">
          <div class="d-flex gap-3" style="align-items: flex-start;">
            <button class="btn btn-primary btn-lg rounded-pill skip-button" (click)="skip()">Skip</button>
            <button class="btn btn-primary btn-lg rounded-pill continue-button" >Continue</button>
          </div>
        </div>
      </div>
    </div>
    <div class="col-xl fixed-bottom" style="background-color: #1976D2; padding: 10px; text-align: center;">
      <div class="color: #1976D2">·</div>
    </div>
  `,
  styles: [`
    .skip-button {
      background: #849AAF;
      width: 120px;
    }

    .continue-button {
      background: #1976D2;
      width: 120px;
    }
  `]
})
export class BotonesBkctComponent {

  constructor(private router: Router) {}

  skip() {
    this.router.navigate(['/home']);
  }

  // @Output() nextPage = new EventEmitter<void>();

  // continue() {
  //   // Emit the countIncremented event to the parent component
  //   this.nextPage.emit();
  // }
}
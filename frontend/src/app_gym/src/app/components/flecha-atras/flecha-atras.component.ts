import { Component } from '@angular/core';

@Component({
  selector: 'app-flecha-atras',
  template: `
    <nav class="navbar bg-body-tertiary">
      <div class="container-fluid">
        <a class="navbar-brand" href="javascript:void(0)" (click)="back()" role="button">
          <div>
            <img src="../../assets/back.svg" alt="configuracion" width="30" height="24" class="d-inline-block align-text-top">
          </div>
        </a>
      </div>
    </nav>
  `,
  styles: []
})
export class FlechaAtrasComponent {
  constructor() {}
  

  back() {
    window.history.back();
  }
}
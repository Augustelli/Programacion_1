import { Component } from '@angular/core';

@Component({
  selector: 'app-nav1',
  templateUrl: './nav1.component.html',
  styleUrls: ['./nav1.component.css']
})
export class Nav1Component {

  routeToHome() {
    window.location.href = '/home';
  }
}

import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-nav2',
  templateUrl: './nav2.component.html',
  styleUrls: ['./nav2.component.css']
})
export class Nav2Component {
  constructor(private router: Router) {}

  redirectLogout(){
  this.router.navigate(['/logout']);
}


}

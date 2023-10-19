import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.css']
})
export class LogoutComponent {

  constructor(private router: Router) {}

cancelLogout() {
  this.router.navigate(['/home']);
}
logout() {
  localStorage.removeItem('token')
  this.router.navigate(['/home']);

}
}

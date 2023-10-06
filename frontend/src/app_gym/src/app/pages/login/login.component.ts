import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  constructor(private route: ActivatedRoute, private router: Router) {
    this.route.queryParams.subscribe(params => {
      if (params['varLogin'] === 'true') {
        // Hacer algo si varLogin es true
      } else {
        // Hacer algo si varLogin es false
      }
    });
  }
  goHomeGuest(){
    this.router.navigate(['/home']);
  }
}


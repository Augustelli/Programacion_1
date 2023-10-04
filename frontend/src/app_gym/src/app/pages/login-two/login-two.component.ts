import { Component } from '@angular/core';
import { LoginThreeComponent } from 'src/app/components/login-three/login-three.component';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-login-two',
  templateUrl: './login-two.component.html',
  styleUrls: ['./login-two.component.css']
})
export class LoginTwoComponent {

  
  constructor(
    private authService: AuthService

  ) { }
  login(dataLogin: any) {
    console.log('comprobando credenciales');
    this.authService.login().subscribe({
      next: (rta:any) => {
        alert('Login correcto');
        console.log('Respuesta Login:',rta);

      },
      error: (err) => {},
      complete: () => {
        console.log('Login finalizado');
      }});

  

}
}


import { Component, OnInit } from '@angular/core';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';

import {  FormGroup ,FormBuilder ,FormControl,  FormGroupDirective,  NgForm,  Validators,  FormsModule,  ReactiveFormsModule,} from '@angular/forms';
import {ErrorStateMatcher} from '@angular/material/core';
import {NgIf} from '@angular/common';

import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';

import { ActivatedRoute, Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';






@Component({
  selector: 'app-login-three',
  templateUrl: './login-three.component.html',
  styleUrls: ['./login-three.component.css'],
  standalone: true,
  imports: [FormsModule, MatFormFieldModule, MatInputModule, ReactiveFormsModule, NgIf ,MatFormFieldModule, MatInputModule, FormsModule, ReactiveFormsModule, NgIf,[MatFormFieldModule, MatInputModule, MatButtonModule, MatIconModule],],
})


export class LoginThreeComponent implements OnInit {
  loginForm!: FormGroup;

  varLogin = false;
  hide = true;
  confirmEmail = new FormControl('', [Validators.required, Validators.email]);
  
  email = new FormControl('', [Validators.required, Validators.email]);
  getErrorMessage() {
    if (this.email.hasError('required')) {
      return 'You must enter a value';
    }

    return this.email.hasError('email') ? 'Not a valid email' : '';
  }
  constructor(private route: ActivatedRoute, 
    private router: Router,
    private authService: AuthService,
    private formBuilder: FormBuilder,
    ) {}
   
  login(dataLogin: any={}) {
    // dataLogin = {email:'admin@example.com', contrasegna:'admin'};
      console.log('comprobando credenciales');
      this.authService.login(dataLogin).subscribe({
        next: (rta:any) => {
          alert('Login correcto');
          console.log('Respuesta Login:',rta.access_token);
          localStorage.setItem('token', rta.access_token);
          this.router.navigate(['/home']);
  
        }, error: (error) => {
          alert('Login incorrecto');
          localStorage.removeItem('token');
          this.router.navigate(['/home']);
        }, complete: () => {
          console.log('Login finalizado');
        }});
      }

ngOnInit() {
  this.route.queryParams.subscribe(params => {
          this.varLogin = params['varLogin'] === 'true';
        });
        
  this.loginForm = this.formBuilder.group({
    email: ['', [Validators.required, Validators.email]],
    contrasegna: ['', [Validators.required, Validators.minLength(3)]],
    // username: ['', [Validators.required, Validators.minLength(5)]],



  }); 
}



redireccionarAcrearUsuario() {
  this.router.navigate(['/crear_usuario']);
}

redireccionarHome() {
  this.router.navigate(['/home']);
}
submit() {
  if (this.loginForm.valid) {

    console.log('Form login: ',this.loginForm.value);
    // console.log('Valid!');
    this.login(this.loginForm.value);
  }else{
    alert('Login incorrecto');
  }
}
}


  
  
  



//   emailFormControl = new FormControl('', [Validators.required, Validators.email]);

//   matcher = new MyErrorStateMatcher();
// }
 
// export class MyErrorStateMatcher implements ErrorStateMatcher {
//   isErrorState(control: FormControl | null, form: FormGroupDirective | NgForm | null): boolean {
//     const isSubmitted = form && form.submitted;
//     return !!(control && control.invalid && (control.dirty || control.touched || isSubmitted));
//   }
// }


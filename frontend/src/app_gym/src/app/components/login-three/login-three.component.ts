import { Component, OnInit } from '@angular/core';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';

import {  FormGroup ,FormBuilder ,AbstractControl ,FormControl,  FormGroupDirective,  NgForm,  Validators,  FormsModule,  ReactiveFormsModule,} from '@angular/forms';
import {ErrorStateMatcher} from '@angular/material/core';
import {NgIf} from '@angular/common';

import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';

import { ActivatedRoute, Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';
import { UsuariosService } from 'src/app/services/usuarios.service';







@Component({
  selector: 'app-login-three',
  templateUrl: './login-three.component.html',
  styleUrls: ['./login-three.component.css'],
  standalone: true,
  imports: [FormsModule, MatFormFieldModule, MatInputModule, ReactiveFormsModule, NgIf ,MatFormFieldModule, MatInputModule, FormsModule, ReactiveFormsModule, NgIf,[MatFormFieldModule, MatInputModule, MatButtonModule, MatIconModule],],
})


export class LoginThreeComponent implements OnInit {
  loginForm!: FormGroup;
  loginForm2!: FormGroup;

  

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
  getErrorMessage1() {
    if (this.email.hasError('required')) {
      return 'You must enter a value';
    }

    return this.email.hasError('email') ? 'Not a valid email' : '';
  }
  

  constructor(private route: ActivatedRoute, 
    private router: Router,
    private authService: AuthService,
    private formBuilder: FormBuilder,
    private usuariosService: UsuariosService,
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
        }, complete: () => {
          console.log('Login finalizado');
        }});
      }

ngOnInit() {
  this.route.queryParams.subscribe(params => {
          this.varLogin = params['varLogin'] === 'true';
        });

        const email = localStorage.getItem('email');
        const contrasegna = localStorage.getItem('contrasegna');
        const nombre = localStorage.getItem('nombre');
        const apellido = localStorage.getItem('apellido');
        const dni = localStorage.getItem('dni');
        
      this.loginForm = this.formBuilder.group({
        email: ['', [Validators.required, Validators.email]],
        contrasegna: ['', [Validators.required, Validators.minLength(3)]],
    

        
      }); 
      
      this.loginForm2 = this.formBuilder.group({
        email: ['', [Validators.required, Validators.email]],
        confirmEmail: ['', [Validators.required, Validators.email]],
        contrasegna: ['', [Validators.required, Validators.minLength(3)]],
        nombre: ['', [Validators.required, Validators.minLength(3)]],
        apellido: ['', [Validators.required, Validators.minLength(3)]],
        dni: ['', [Validators.required, Validators.minLength(8), Validators.pattern(/^\d{8}$/)]],
      });


    }




    
submit() {
  if (this.loginForm.valid) {

    console.log('Form login: ',this.loginForm.value);
    this.login(this.loginForm.value);
    
  }else{
    alert('Login incorrecto');
  }
}



submit2() {
  if (this.loginForm2.valid) {
    const email = this.loginForm2.get('email')?.value;
    const confirmEmail = this.loginForm2.get('confirmEmail')?.value;
    const contrasegna = this.loginForm2.get('contrasegna')?.value;
    const nombre = this.loginForm2.get('nombre')?.value;
    const apellido = this.loginForm2.get('apellido')?.value;
    const dni = this.loginForm2.get('dni')?.value;

    if (email !== confirmEmail) {
      alert('Los correos no coinciden');
      return;
    }

    // Verificar si el correo ya existe en el backend
    this.usuariosService.checkEmailExists(email).subscribe((response: any) => {
      console.log('Respuesta checkEmailExists: ', response);
      if (Array.isArray(response) && response.length > 0 && response[0].email === email) {
        // Resto del código
        alert('El correo electrónico ya está registrado. Por favor, elige otro correo.');
      } else {
        // Verificar si el DNI ya existe en el backend
        this.usuariosService.checkDniExists(dni).subscribe((response:any) => {
          console.log('Respuesta checkDniExists: ', response);
          if (Array.isArray(response) && response.length > 0) {
            alert('El número de DNI ya está registrado. Por favor, elige otro número de DNI.');
          } else {
            // Continuar con el registro si el correo y el DNI no existen
            if (email && contrasegna && nombre && apellido && dni) {
              localStorage.setItem('email', email);
              localStorage.setItem('contrasegna', contrasegna);
              localStorage.setItem('nombre', nombre);
              localStorage.setItem('apellido', apellido);
              localStorage.setItem('dni', dni);

              this.router.navigate(['/crear_usuario']);
            } else {
              alert('Algunos campos son nulos o inválidos');
            }
          }
        });
      }
    });
  } else {
    alert('Login incorrecto');
  }
}
}



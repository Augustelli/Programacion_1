// import { Component } from '@angular/core';
// import {
//   FormControl,
//   FormGroupDirective,
//   NgForm,
//   Validators,
// } from '@angular/forms';
// import { ErrorStateMatcher } from '@angular/material/core';

// export class MyErrorStateMatcher implements ErrorStateMatcher {
//   isErrorState(control: FormControl | null, form: FormGroupDirective | NgForm | null): boolean {
//     const isSubmitted = form && form.submitted;
//     return !!(
//       control &&
//       (control.invalid || (control.value !== form.controls['password'].value && form.controls['repeatPassword'].touched)) &&
//       (control.dirty || control.touched || isSubmitted)
//     );
//   }
// }
// @Component({
//   selector: 'app-crar-usuario-main',
//   templateUrl: './crar-usuario-main.component.html',
//   styleUrls: ['./crar-usuario-main.component.css']
// })

// export class CrearUsuarioComponent {
//   emailFormControl = new FormControl('', [
//     Validators.required,
//     Validators.email,
//   ]);

//   usernameFormControl = new FormControl('', [
//     Validators.required,
//     Validators.minLength(8),
//     Validators.maxLength(22),
//   ]);

//   passwordFormControl = new FormControl('', [
//     Validators.required,
//     Validators.minLength(8),
//     Validators.maxLength(32),
//     Validators.pattern(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$/),
//   ]);

//   repeatPasswordFormControl = new FormControl('', [
//     Validators.required,
//   ]);

//   matcher = new MyErrorStateMatcher();
// }
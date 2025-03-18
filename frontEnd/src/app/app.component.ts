import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

import { CommonModule } from '@angular/common';
import {HttpClientModule, HttpClient} from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
@Component({
  selector: 'app-root',
  imports: [RouterOutlet, CommonModule, HttpClientModule, FormsModule, ReactiveFormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Alfred';

  students: any = [];
  ApiUrl = 'http://localhost:8000/';
  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.getStudents();
  }
  getStudents() {
    this.http.get(this.ApiUrl+"student").subscribe((response) => {
      this.students = response;
    });
  }
}

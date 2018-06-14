import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { provideRoutes, RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
import {
  MatButtonModule,
  MatFormFieldModule,
  MatInputModule,
  MatSelectModule,
  MatToolbarModule
} from '@angular/material'

import { AppComponent } from './app.component';
import { CalcuratorComponent } from './calcurator/calcurator.component';
import { AppRoutingModule } from './app-routing.module';


@NgModule({
  declarations: [
    AppComponent,
    CalcuratorComponent
  ],
  imports: [
    AppRoutingModule,
    BrowserModule,
    BrowserAnimationsModule,
    FormsModule,
    HttpClientModule,
    MatButtonModule,
    MatInputModule,
    MatFormFieldModule,
    MatSelectModule,
    MatToolbarModule,
    RouterModule,
  ],
  providers: [
    {provide: 'ApiEndpoint', useValue: 'http://localhost:3000/'}
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

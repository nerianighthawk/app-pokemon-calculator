import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router'

import { CalcuratorComponent } from './calcurator/calcurator.component';

const routes: Routes = [
  { path: 'calcurator', component: CalcuratorComponent }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes)
  ],
  declarations: []
})
export class AppRoutingModule { }

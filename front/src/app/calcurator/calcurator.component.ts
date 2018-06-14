import { Component, OnInit, Inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-calcurator',
  templateUrl: './calcurator.component.html',
  styleUrls: ['./calcurator.component.css']
})
export class CalcuratorComponent implements OnInit {

  public pokemons: any;

  constructor(
    @Inject('ApiEndpoint') private api_path: string,
    private http: HttpClient,
  ) { }

  ngOnInit() {
    this.http.get(this.api_path + "getPokemon").subscribe(
      json => {
        this.pokemons = json['data'];
      }
    )
  }

}

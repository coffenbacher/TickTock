/* 
 * MapTips, v1.0
 * Author: Klaus Paiva (blog.klaus.pro.br)
 *
 * Copyright 2008, Klaus Paiva 
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License. 
*/

$.fn.extend(
	{
		// http://www.quirksmode.org/js/findpos.html
		find_pos : function()
		{
			if( !this.tagName && this.length )
			{
				obj = this[0];
			}
			else
			{
				return [0,0];
			}
			var curleft = curtop = 0;
			if (obj.offsetParent) {
				curleft = obj.offsetLeft;
				curtop = obj.offsetTop;
				while (obj = obj.offsetParent) {
					curleft += obj.offsetLeft;
					curtop += obj.offsetTop;
				}
			}
			return [curleft,curtop];
		}
	}
);

function MapTips( map )
{
	var self = this;
	var _map = map;
	this.add_tooltip = function( marker, text )
	{
		marker.tooltip = text;
		GEvent.addListener( marker, "mouseover", self.show_tooltip );
		GEvent.addListener( marker, "mouseout", self.hide_tooltip );
	};
	this.show_tooltip = function( marker )
	{
		// obtêm o x e y do marcador
		var marker_point = _map.fromLatLngToContainerPixel( this.getLatLng() );
		$( "body" ).append( '<p id="maptip" style="visibility: hidden;">' + this.tooltip + '</p>' );
		// pega a posição do mapa atual do mapa, em x e y.
		var positions = $( _map.getContainer() ).find_pos();
		
		// calcula os três pontos para reposicionamento no mapa: left, right e top
		var map_left = positions[0];
		var map_right = positions[0] + $( _map.getContainer() ).width();
		var map_top = positions[1];
		
		// captura o tamanho do ícone para fazer o posicionamento
		var icon_size = this.getIcon().iconSize;
		positions[0] += marker_point.x;
		positions[1] += marker_point.y - icon_size.height;
		var x_adjustment = $( "#maptip" )[0].offsetWidth / 2; // divide por 2 para ficar centralizado
		var y_adjustment = $( "#maptip" )[0].offsetHeight + 3;
		var left_value = positions[0] - x_adjustment; // calculo do valor "left" da maptip
		var top_value = positions[1] - y_adjustment // calculo do valor "top" da maptip
		
		// aqui são feitos os cálculos para corrigir o posicionamento quando a maptip aparece nos cantos do mapa
		// não há necessidade de alterar esses valores
		var tip_left = positions[0] - x_adjustment;
		var tip_right = positions[0] - x_adjustment + $( "#maptip" )[0].offsetWidth;
		var tip_top = positions[1] - y_adjustment;
		if( map_left >= tip_left )
		{
			left_value += map_left - tip_left + 3; // + 3 é para a borda não colar na borda do mapa
		}
		else if( map_right <= tip_right )
		{
			left_value -= tip_right - map_right + 3; // + 3 é para a borda não colar na borda do mapa
		}
		if( map_top >= tip_top )
		{
			top_value += $( "#maptip" )[0].offsetHeight + icon_size.height + 6; // coloca abaixo do marcador
		}
		
		// por fim, atribui os valores calculados e exibe a maptip
		$( "#maptip" ).css( "left", left_value ).css( "top", top_value ).css( "visibility", "visible" );
		$( "#maptip" ).fadeIn( "medium" );
	};
	this.hide_tooltip = function()
	{
		$( "#maptip" ).remove();
	};
}

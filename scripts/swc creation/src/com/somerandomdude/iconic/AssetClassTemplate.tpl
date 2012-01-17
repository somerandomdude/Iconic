package com.somerandomdude.iconic {
	
	/**
	 * ...
	 * @author P.J. Onori
	 */
	
	import flash.display.DisplayObject;
	import flash.display.Sprite;
	
	public class Iconic_@ASSET_NAME@ extends Sprite {
		
		
		[Embed(source='@ASSET_PATH@/@ASSET_NAME@.@ASSET_EXTENSION@')]
		private static var IconAsset:Class;
		
		public function Iconic_@ASSET_NAME@() {
			super();
			
			addChild(DisplayObject(new IconAsset()));
			return;
		}
	}
}
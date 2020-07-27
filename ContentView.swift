//
//  ContentView.swift
//  SwiftUitest
//
//  Created by veenjain on 6/23/20.
//  Copyright © 2020 veenjain. All rights reserved.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        
        ZStack {
            Rectangle()
                .foregroundColor(Color(red:200/255, green: 143/255, blue: 32/255))
                .edgesIgnoringSafeArea(.all)
            
            Rectangle()
                .foregroundColor(Color(red:228/255, green:196/255, blue:64/225))
                .rotationEffect(Angle(degrees:45))
                .edgesIgnoringSafeArea(.all)
            
            VStack {
                Text("Hi")
                HStack {
                    Image(systemName: "star.fill")
                        .foregroundColor(.yellow)
                    
                    Text("Social Distancing App")
                        .bold()
                        .foregroundColor(.white)
                }.scaleEffect(2)
                
        }
        //.padding(10)
        //.cornerRadius(20)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
}

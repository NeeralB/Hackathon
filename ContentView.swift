//
//  ContentView.swift
//  SocialDistancingApp
//
//  Created by veenjain on 6/29/20.
//  Copyright © 2020 veenjain. All rights reserved.
//

import SwiftUI  

struct ContentView: View {
    var body: some View {
        
        ZStack {
            Rectangle()
                .foregroundColor(Color(red: 200/255, green: 143/255, blue: 32/355))
                .edgesIgnoringSafeArea(.all)
            
            Rectangle()
                .foregroundColor(Color(red:228/255, green: 195/255, blue: 76/255))
                .rotationEffect(Angle(degrees:45))
                .edgesIgnoringSafeArea(.all)
            
            VStack {
                
                HStack {
                    Image(systemName: "star.fill").foregroundColor(.pink)
                    
                    Text("Secure your Space!").bold()
                        .foregroundColor(.white)
                    
                    Image(systemName: "star.fill").foregroundColor(.pink)
                }.scaleEffect(2.0)
                
                
                Text("The app that verifies ").foregroundColor(.black)
                    .padding(.all,10)
                    .font(.largeTitle)
                Text("social distancing").foregroundColor(.black)
                    .font(.largeTitle)
            
                
                VStack {
                    Image("Social Distancing")
                        .resizable()
                        .aspectRatio(1,contentMode: .fit)
                        .cornerRadius(20)
                        .offset(y:90)
                    Image("social distance-1")
                        .resizable()
                        .aspectRatio(1,contentMode: .fit)
                        .cornerRadius(10)
                        .offset(y:85)
                        Spacer()
                }.scaleEffect(1.25)
                
                
                Button(action: {
                    
                
                }) {
                    Text("You are not social distancing")
                    .bold()
                        .foregroundColor(.white)
                        .padding(.all,10)
                        .padding([.leading,.trailing],30)
                        .padding()
                        
                        .background(Color.pink)
                    .cornerRadius(20)
                }.scaleEffect(1.25)
            
            
            
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
}


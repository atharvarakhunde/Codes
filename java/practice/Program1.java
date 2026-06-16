// // AO FM JJ MF OA
// //    BN GK KG NB
// //       CL HH LC
// //          DI ID
// //             EE

// // 1 6 10 13 15
// //   2  7 11 14
// //      3  8 12
// //         4  9
// //            5

// // 15 13 10 6 1
// //    14 11 7 2
// //       12 8 3
// //          9 4
// //            5

// public class Program1 {
//     public static void main (String args[]){
//         int n = 5;
//         int count1= 1;
//         int count2= ((n*(n+1))/2);
//         for(int i=1;i<=n;i++){
//             int c1 = count1;
//             int c2 = count2;
//             for (int j=i;j>1;j--){
//                 System.out.print("  ");
//             }
//             for(int j=n, j1 = i ;j>=i|| j1<=n;j--,j1++){
//                 System.out.print((char)(c1+64) );
//                 System.out.print((char)(c2+64 ));
//                 System.out.print("  ");
//                 c1+=j;
//                 c2-=j1+1;
//             }
//             System.out.println();
//             count1++;
//             count2-=i;
//         }
//     }
// }

// // OO NJ LF IC EA
// // MN KI HE DB
// // JM GH CD
// // FL BG
// // AK

// // 15 14 12 9 5
// // 13 11  8 4  
// // 10  7  3  
// //  6  2
// //  1      

// 15 10 6 3 1
// 14  9 5 2
// 13  8 4
// 12  7
// 11

// public class Program1{
//     public static void main (String args[]){
//         int n = 5;
//         int count1= ((n*(n+1))/2);
//         int count2= ((n*(n+1))/2);
//         for(int i=1;i<=n;i++){
//             int c1 = count1;
//             int c2 = count2;
//             for(int j=i,j1=n;j<=n|| j1>=i;j++,j1--){
//                 System.out.print((char)(c1+64) );
//                 System.out.print((char)(c2+64 ));
//                 System.out.print("  ");
//                 c1-=j;
//                 c2-=j1;
//             }
//             System.out.println();
//             count1-=i+1;
//             count2--;
//         }

        
//     }
// }

//             EO
//          IJ DN
//       LF HI CM
//    NC KE GH BL
// OA MB JD FG AK

//              5
//           9  4
//       12  8  3
//    14 11  7  2
// 15 13 10  6  1   

//             15
//          10 14
//        6  9 13
//     3  5  8 12
//  1  2  4  7 11

// public class Program1{
//     public static void main (String args[]){
//         int n = 5;
//         int count1= n;
//         int count2= ((n*(n+1))/2);
//         for(int i=n;i>=1;i--){
//             int c1 = count1;
//             int c2 = count2;
//             for(int j=i ; j>=1;j--){
//                 System.out.print("    ");
//             }
//             for(int j=i;j<=n;j++){
//                 System.out.print((char)(c1+64));
//                 System.out.print((char)(c2+64));
//                 System.out.print("  ");
//                 c1-=j+1;
//                 c2+=j;
//             }
//             System.out.println();
//             count1+=i-1;
//             count2-=i;
//         }
//     }
// }


//             OA
//          JC NB
//       FF IE MD
//    CJ EI HH LG
// AO BN DM GL KK 

//             15
//          10 14
//        6  9 13
//     3  5  8 12
//  1  2  4  7 11 

//              1
//           3  2
//        6  5  4
//    10  9  8  7
// 15 14 13 12 11



// public class Program1{
//     public static void main (String args[]){
//         int n = 5;
//         int count1= ((n*(n+1))/2);
//         int count2= 1;
//         for(int i=n, i1 =1;i>=1||i1<=n;i--,i1++){
//             int c1 = count1;
//             int c2 = count2;
//             for(int j=i ; j>=1;j--){
//                 System.out.print("    ");
//             }
//             for(int j=i,j1=i1;j<=n||j1>=1;j++,j1--){
//                 System.out.print((char)(c1+64));
//                 System.out.print((char)(c2+64));
//                 System.out.print("  ");
//                 c1+=j;
//                 c2--;
//             }
//             System.out.println();
//             count1-=i;
//             count2+=i1+1;
//         }

        
//     }
// }


// Ea Db Cd Bg Ak
// Ic He Gh Fl
// Lf Ki Jm
// Nj Mn
// Oo

//  5  4  3  2  1
//  9  8  7  6
// 12 11 10
// 14 13
// 15

//  1  2  4  7 11
//  3  5  8 12
//  6  9 13
// 10 14
// 15



// public class Program1{
//     public static void main (String args[]){
//         int n = 5;
//         int count1= n;
//         int count2= 1;
//         for(int i=n, i1 =1;i>=1||i1<=n;i--,i1++){
//             int c1 = count1;
//             int c2 = count2;
//             for(int j=i,j1=i1;j>=1||j1<=n;j--,j1++){
//                 System.out.print((char)(c1+64));
//                 System.out.print((char)(c2+96));
//                 System.out.print("  ");
//                 c1--;
//                 c2+=j1;
//             }
//             System.out.println();
//             count1+=i-1;
//             count2+=i1+1;
//         }

        
//     }
// }


// EE DI CL BN AO
// ID HH GK FM
// LC KG JJ
// NB MF
// OA


//  5  4  3  2  1
//  9  8  7  6
// 12 11 10
// 14 13
// 15

//  5  9 12 14 15
//  4  8 11 13
//  3  7 10
//  2  6
//  1



// public class Program1{
//     public static void main (String args[]){
//         int n = 5;
//         int count1= n;
//         int count2= n;
//         for(int i=n, i1 =1;i>=1||i1<=n;i--,i1++){
//             int c1 = count1;
//             int c2 = count2;
//             for(int j=i,j1=n;j>=1||j1>=i1;j--,j1--){
//                 System.out.print((char)(c1+64));
//                 System.out.print((char)(c2+64));
//                 System.out.print("  ");
//                 c1--;
//                 c2+=j1-1;
//             }
//             System.out.println();
//             count1+=i-1;
//             count2--;
//         }

        
//     }
// }













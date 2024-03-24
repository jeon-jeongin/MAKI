"use client";
import "./globals.css";
import Header from "./Header";

// export default function RootLayout() {
//   return (
//     <>
//       <Header />
//     </>
//   );
// }

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <Header />
      </body>
    </html>
  );
}

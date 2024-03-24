"use client";
/** @jsxImportSource @emotion/react */

import { css } from "@emotion/react";

// 상수 정의
const IMAGES_PATH = "/images";
const headerContainerStyle = css`
  justify-content: space-between;
  padding-left: 3.125rem;
  padding-right: 3.125rem;
  position: relative;
  display: flex;
  align-items: center;
  height: 4rem;
`;

const logoStyle = css`
  display: block;
  max-width: 100%;
  height: 1.8rem;
`;

const searchStyle = css`
  display: block;
  width: 1.5rem;
  height: 1.5rem;
`;

const menuItemStyle = css`
  margin-left: 1.5rem;
  display: flex;
  align-items: center;
  font-size: 0.875rem;
`;

export default function Header() {
  return (
    <header>
      <div css={headerContainerStyle}>
        <div
          css={css`
            display: flex;
          `}
        >
          <div css={logoStyle}>
            <img
              css={css`
                width: 100%;
                height: 100%;
              `}
              src={`${IMAGES_PATH}/logo.png`}
              alt="로고이미지"
            />
          </div>
          <div
            css={css`
              margin-left: 2.25rem;
              display: flex;
              position: relative;
            `}
          >
            <p css={menuItemStyle}>태그검색</p>
            <p css={menuItemStyle}>요일별 신작</p>
            <p css={menuItemStyle}>테마추천</p>
          </div>
        </div>
        <div
          css={css`
            display: flex;
          `}
        >
          <div css={searchStyle}>
            <img
              css={css`
                width: 100%;
                height: 100%;
              `}
              src={`${IMAGES_PATH}/searchbar-icon.png`}
              alt="로고이미지"
            />
          </div>
          {/* <p>돋보기 넣기</p> */}
          <p css={menuItemStyle}>로그인/가입</p>
        </div>
      </div>
    </header>
  );
}

// const IMAGES_PATH = "/images";
// import { css } from "@emotion/react";

// export default function Header() {
//   return (
//     <header>
//       <div
//         css={css`
//           justify-content: space-between;
//           padding-left: 3.125rem;
//           padding-right: 3.125rem;
//           position: relative;
//           display: flex;
//           -webkit-box-align: center;
//           align-items: center;
//           height: 4rem;
//         `}
//       >
//         <div
//           css={css`
//             display: flex;
//           `}
//         >
//           <div
//             css={css`
//               display: block;
//               max-width: 100%;
//               height: 2rem;
//             `}
//           >
//             <img
//               css={css`
//                 width: 100%;
//                 height: 100%;
//               `}
//               src={`${IMAGES_PATH}/logo.png`}
//               alt="로고이미지"
//             />
//           </div>
//           <div
//             css={css`
//               margin-left: 2.5rem;
//               display: flex;
//               position: relative;
//             `}
//           >
//             <p
//               css={css`
//                 margin-left: 1.5rem;
//                 display: flex;
//                 align-items: center;
//               `}
//             >
//               태그검색
//             </p>
//             <p
//               css={css`
//                 margin-left: 1.5rem;
//                 display: flex;
//                 align-items: center;
//               `}
//             >
//               요일별 신작
//             </p>
//             <p
//               css={css`
//                 margin-left: 1.5rem;
//                 display: flex;
//                 align-items: center;
//               `}
//             >
//               테마추천
//             </p>
//           </div>
//         </div>
//         <div
//           css={css`
//             display: flex;
//           `}
//         >
//           <p>돋보기 넣기</p>
//           <p
//             css={css`
//               margin-left: 1.5rem;
//             `}
//           >
//             로그인/가입
//           </p>
//         </div>
//       </div>
//     </header>
//   );
// }

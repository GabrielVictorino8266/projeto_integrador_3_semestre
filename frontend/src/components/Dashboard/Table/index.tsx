import type React from "react";

interface IDashboardTableProps {
  children: React.ReactNode;
  title: string;
  thTitles: Array<string>;
}

const DashboardTable = ({
  children,
  title,
  thTitles,
}: IDashboardTableProps) => {
  const thElements = thTitles.map((title) => {
    return <th key={title}>{title}</th>;
  });

  return (
    <div>
      <div>
        <h2 className="list__title">{title}</h2>
      </div>
      <table>
        <thead>
          <tr>{thElements}</tr>
        </thead>
        {children}
      </table>
    </div>
  );
};

export { DashboardTable };

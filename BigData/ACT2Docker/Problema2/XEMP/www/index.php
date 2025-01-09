<?php
include "consulta.php";
?>
<!doctype html>
<html lang="en">

<head>
    <title>Pila XEMP</title>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta
        name="viewport"
        content="width=device-width, initial-scale=1, shrink-to-fit=no" />

    <!-- Bootstrap CSS v5.2.1 -->
    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
        rel="stylesheet"
        integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
        crossorigin="anonymous" />
    <script defer
        src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"
        integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r"
        crossorigin="anonymous"></script>
    <script defer
        src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js"
        integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+"
        crossorigin="anonymous"></script>
</head>

<body>
    <header>
        <!-- place navbar here -->
    </header>
    <main>
        <h1 class="fw-light text-center mt-5 mb-5 ">Usuarios</h1>
        <div class="container">
        <div
            class="table-responsive">
            <table
                class="table table-primary">
                <thead>
                    <tr class='p-2'>
                        <?php
                        foreach ($rows[0] as $columnName => $value) {
                            echo "<th>$columnName</th>";
                        }
                        ?>
                    </tr>
                </thead>
                <tbody>
                    <?php
                    foreach ($rows as $row) {
                        echo "<tr>";
                        foreach ($row as $key => $value) {
                            echo "<td>$value</td>";
                        }
                        echo "</tr>";
                    }
                    ?>
                </tbody>
            </table>
        </div>      
        </div>
        

    </main>
    <footer>
        <!-- place footer here -->
    </footer>
    <!-- Bootstrap JavaScript Libraries -->



</body>

</html>
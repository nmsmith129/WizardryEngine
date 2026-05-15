#!/usr/bin/perl
use strict;
use warnings;

# ANSI color codes
my $RESET = "\e[0m";
my $RED = "\e[31;1m";    # Bright red for walls
my $GREEN = "\e[32;1m";  # Bright green for entrance
my $BLUE = "\e[34;1m";   # Bright blue for exit


# Get terminal size
my $size = `stty size`;
my ($height, $width) = split(/\s+/, $size);

$width -= 1;
$height -= 1;

# Adjust for maze walls (odd numbers for paths)
$width = $width - 1 if $width % 2 == 0;
$height = $height - 1 if $height % 2 == 0;

# Fancy maze characters
my $wall_char = '#';  # Full block for walls
my $path_char = ' ';  # Empty space for paths
my $entry_char = 'E'; # Entrance
my $exit_char  = 'X'; # Exit

# Maze grid
my @maze = map { [ ($wall_char) x $width ] } 1 .. $height;

# Directions for movement (right, left, down, up)
my @directions = (
    [ 0,  2],  # right
    [ 0, -2],  # left
    [ 2,  0],  # down
    [-2,  0]   # up
);

# Maze generation using non-recursive backtracking (stack-based)
sub generate_maze {
    my ($start_x, $start_y) = @_;

    # Stack to simulate recursion
    my @stack = ([$start_x, $start_y]);

    # Mark the start point as a path
    $maze[$start_y][$start_x] = $path_char;

    while (@stack) {
        my ($x, $y) = @{ pop @stack };

        # Shuffle directions to create randomness
        my @shuffled_directions = sort { rand() <=> rand() } @directions;

        my $moved = 0;
        foreach my $dir (@shuffled_directions) {
            my ($dx, $dy) = @$dir;

            my $nx = $x + $dx;
            my $ny = $y + $dy;

            # Check if new position is inside the maze bounds
            if ($nx > 0 && $nx < $width - 1 && $ny > 0 && $ny < $height - 1) {
                # Check if the cell hasn't been visited yet (is a wall)
                if ($maze[$ny][$nx] eq $wall_char) {
                    # Knock down the wall
                    $maze[$y + $dy / 2][$x + $dx / 2] = $path_char;
                    $maze[$ny][$nx] = $path_char;

                    # Push the current position and the new position onto the stack
                    push @stack, [$x, $y];  # Current position
                    push @stack, [$nx, $ny]; # Move to new position

                    $moved = 1;
                    last;
                }
            }
        }
    }
}

# Add entrance and exit to the maze
sub add_entrance_exit {
    # Entrance at the top left corner
    $maze[1][0] = $entry_char;

    # Exit at the bottom right corner
    $maze[$height-2][$width-1] = $exit_char;
}

# Start maze generation from the top-left corner (1,1)
generate_maze(1, 1);

# Add the entrance and exit to the maze
add_entrance_exit();

# Print the colorful maze
for my $row (@maze) {
    for my $cell (@$row) {
        if ($cell eq $wall_char) {
            # Print wall with red color
            print "${RED}${wall_char}${RESET}";
        } elsif ($cell eq $entry_char) {
            # Print entrance with green color
            print "${GREEN}${entry_char}${RESET}";
        } elsif ($cell eq $exit_char) {
            # Print exit with blue color
            print "${BLUE}${exit_char}${RESET}";
        } else {
            # Print path as normal
            print $path_char;
        }
    }
    print "\n";
}
One more try
steven smith<smith2854@charter.net>
​You​

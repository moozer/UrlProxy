#!/bin/sh

echo "Doing simple sanity tests of rot13"

in1="HELLO"
out1="URYYB"
in2="hello"
out2="uryyb"

# Define your function here
test_rot13 () {
	in=$1
	out=$2

	echo "checking set $in and $out"

	res_out=$(echo $in | ./rot13.bin)
	if [ "$out" = "$res_out" ]; then
		echo "test ok. rot13($in) == $res_out"
	else
		echo "test failed. rot13($in) == $out, but was reported as $res_out"
	fi

	dout=$(echo $res_out | ./rot13.bin)
	if [ "$dout" = "$in" ]; then
		echo "test ok. rot13(rot13($in)) == $in"
	else
		echo "test failed. rot13(rot13($in)) == $in, but was reported as $dout"
	fi
}

test_rot13 $in1 $out1
test_rot13 $in2 $out2
